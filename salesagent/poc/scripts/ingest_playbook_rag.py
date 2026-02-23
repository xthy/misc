#!/usr/bin/env python3
"""
B2B Sales Agent — Playbook RAG Ingestion Script

Markdown 문서를 섹션 단위로 청킹하여 playbook_chunks 테이블에 적재합니다.
Embedding은 OpenAI text-embedding-3-small (1536 dim) 사용.

Usage:
    # Dry run (chunking만 확인, DB 미적재)
    python3 ingest_playbook_rag.py --dry-run

    # 실제 적재 (DB + embedding)
    python3 ingest_playbook_rag.py

    # 특정 파일만
    python3 ingest_playbook_rag.py --files playbook/02_meddicc_guide.md

    # Embedding 없이 텍스트만 적재
    python3 ingest_playbook_rag.py --skip-embedding

Requirements:
    pip install psycopg2-binary openai
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Optional

# ─── Configuration ───────────────────────────────────────────

# Project root (relative to this script's location)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # poc/scripts/ → salesagent/

# Files to ingest (relative to PROJECT_ROOT)
DEFAULT_FILES = [
    # Playbook core
    "playbook/00_sales_process_canon.md",
    "playbook/01_icp_and_scoring.md",
    "playbook/02_meddicc_guide.md",
    "playbook/03_call_scripts.md",
    "playbook/04_email_templates.md",
    "playbook/05_objection_handling.md",
    "playbook/06_competitive_battle_card.md",
    "playbook/07_pricing_discount_matrix.md",
    "playbook/08_sales_onboarding_curriculum.md",
    # Plays
    "playbook/plays/play_01_new_logo_outbound_t2t3.md",
    "playbook/plays/play_02_strategic_account_expansion_t1.md",
    "playbook/plays/play_03_renewal_rescue.md",
    "playbook/plays/play_04_cs_driven_upsell.md",
    "playbook/plays/play_05_win_loss_analysis.md",
    "playbook/plays/play_06_inbound_lead_handling.md",
    "playbook/plays/play_07_partner_channel_sales.md",
    # Agent specs
    "agent/01_qualification_agent.md",
    "agent/02_orchestration_agent.md",
    "agent/03_lead_generation_agent.md",
    "agent/04_deal_conversion_agent.md",
    "agent/05_customer_success_agent.md",
    # CRM schema
    "crm/schema.md",
    # Research
    "research/01_kpi_benchmarks.md",
    "research/02_ai_sales_agent_cases.md",
    "research/03_tech_stack_comparison.md",
]

# Chunking parameters
MAX_CHUNK_CHARS = 1500     # Target chunk size (characters)
MIN_CHUNK_CHARS = 100      # Skip chunks smaller than this
OVERLAP_CHARS = 200        # Overlap between consecutive chunks in same section

# Database
DB_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": int(os.getenv("PG_PORT", "5432")),
    "dbname": os.getenv("PG_DB", "salesagent"),
    "user": os.getenv("PG_USER", "salesagent"),
    "password": os.getenv("PG_PASSWORD", "salesagent_dev"),
}

# Embedding
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIM = 1536


# ─── Chunking Logic ──────────────────────────────────────────

def parse_markdown_sections(text: str, source_file: str) -> list[dict]:
    """Split markdown into sections by ## and ### headings."""
    lines = text.split("\n")
    sections = []
    current_section = {
        "title": "(top)",
        "level": 0,
        "lines": [],
    }

    for line in lines:
        # Detect heading
        heading_match = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading_match:
            # Save previous section if it has content
            content = "\n".join(current_section["lines"]).strip()
            if content and len(content) >= MIN_CHUNK_CHARS:
                sections.append({
                    "title": current_section["title"],
                    "level": current_section["level"],
                    "content": content,
                })

            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            current_section = {
                "title": title,
                "level": level,
                "lines": [],
            }
        else:
            current_section["lines"].append(line)

    # Don't forget the last section
    content = "\n".join(current_section["lines"]).strip()
    if content and len(content) >= MIN_CHUNK_CHARS:
        sections.append({
            "title": current_section["title"],
            "level": current_section["level"],
            "content": content,
        })

    return sections


def chunk_section(section: dict, source_file: str, start_index: int) -> list[dict]:
    """Split a section into chunks if it exceeds MAX_CHUNK_CHARS."""
    content = section["content"]
    title = section["title"]
    chunks = []

    if len(content) <= MAX_CHUNK_CHARS:
        chunks.append({
            "source_file": source_file,
            "section_title": title,
            "chunk_text": content,
            "chunk_index": start_index,
            "metadata": {
                "heading_level": section["level"],
                "char_count": len(content),
            },
        })
    else:
        # Split by paragraphs first, then by sentences if needed
        paragraphs = content.split("\n\n")
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) + 2 <= MAX_CHUNK_CHARS:
                current_chunk = (current_chunk + "\n\n" + para).strip()
            else:
                if current_chunk and len(current_chunk) >= MIN_CHUNK_CHARS:
                    chunks.append({
                        "source_file": source_file,
                        "section_title": title,
                        "chunk_text": current_chunk,
                        "chunk_index": start_index + len(chunks),
                        "metadata": {
                            "heading_level": section["level"],
                            "char_count": len(current_chunk),
                            "is_split": True,
                        },
                    })
                # Start new chunk with overlap
                if OVERLAP_CHARS > 0 and current_chunk:
                    overlap = current_chunk[-OVERLAP_CHARS:]
                    current_chunk = overlap + "\n\n" + para
                else:
                    current_chunk = para

        # Last chunk
        if current_chunk and len(current_chunk) >= MIN_CHUNK_CHARS:
            chunks.append({
                "source_file": source_file,
                "section_title": title,
                "chunk_text": current_chunk.strip(),
                "chunk_index": start_index + len(chunks),
                "metadata": {
                    "heading_level": section["level"],
                    "char_count": len(current_chunk),
                    "is_split": len(chunks) > 0,
                },
            })

    return chunks


def process_file(filepath: Path, source_file: str) -> list[dict]:
    """Read a markdown file and return all chunks."""
    text = filepath.read_text(encoding="utf-8")
    sections = parse_markdown_sections(text, source_file)

    all_chunks = []
    chunk_index = 0
    for section in sections:
        new_chunks = chunk_section(section, source_file, chunk_index)
        all_chunks.extend(new_chunks)
        chunk_index += len(new_chunks)

    return all_chunks


# ─── Embedding ────────────────────────────────────────────────

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Generate embeddings using OpenAI API."""
    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: openai package not installed. Run: pip install openai")
        sys.exit(1)

    client = OpenAI()  # Uses OPENAI_API_KEY env var
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]


# ─── Database ─────────────────────────────────────────────────

def get_db_connection():
    """Connect to PostgreSQL."""
    try:
        import psycopg2
    except ImportError:
        print("ERROR: psycopg2 package not installed. Run: pip install psycopg2-binary")
        sys.exit(1)

    return psycopg2.connect(**DB_CONFIG)


def clear_existing_chunks(conn, source_files: list[str]):
    """Delete existing chunks for the specified source files."""
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM playbook_chunks WHERE source_file = ANY(%s)",
            (source_files,)
        )
    conn.commit()


def insert_chunks(conn, chunks: list[dict], embeddings: Optional[list] = None):
    """Insert chunks into playbook_chunks table."""
    with conn.cursor() as cur:
        for i, chunk in enumerate(chunks):
            embedding = embeddings[i] if embeddings else None
            cur.execute(
                """
                INSERT INTO playbook_chunks
                    (source_file, section_title, chunk_text, chunk_index, embedding, metadata)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    chunk["source_file"],
                    chunk["section_title"],
                    chunk["chunk_text"],
                    chunk["chunk_index"],
                    str(embedding) if embedding else None,
                    json.dumps(chunk["metadata"]),
                ),
            )
    conn.commit()


# ─── Main ─────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Ingest playbook markdown docs into RAG vector store"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chunk only, don't write to DB or generate embeddings",
    )
    parser.add_argument(
        "--skip-embedding",
        action="store_true",
        help="Insert text chunks without generating embeddings",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        help="Specific files to ingest (relative to project root)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Embedding API batch size (default: 50)",
    )
    args = parser.parse_args()

    files_to_process = args.files if args.files else DEFAULT_FILES

    print("=" * 60)
    print(" B2B Sales Agent — Playbook RAG Ingestion")
    print("=" * 60)
    print(f"\nProject root: {PROJECT_ROOT}")
    print(f"Files to process: {len(files_to_process)}")
    print(f"Max chunk size: {MAX_CHUNK_CHARS} chars")
    print(f"Overlap: {OVERLAP_CHARS} chars")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    # Process all files
    all_chunks = []
    for rel_path in files_to_process:
        filepath = PROJECT_ROOT / rel_path
        if not filepath.exists():
            print(f"  SKIP: {rel_path} (not found)")
            continue

        chunks = process_file(filepath, rel_path)
        all_chunks.extend(chunks)
        print(f"  OK: {rel_path} → {len(chunks)} chunks")

    print(f"\nTotal chunks: {len(all_chunks)}")

    # Stats
    total_chars = sum(len(c["chunk_text"]) for c in all_chunks)
    avg_chars = total_chars // len(all_chunks) if all_chunks else 0
    print(f"Total characters: {total_chars:,}")
    print(f"Average chunk size: {avg_chars} chars")
    print(f"Estimated tokens: ~{total_chars // 4:,}")

    if args.dry_run:
        print("\n--- DRY RUN: Showing first 5 chunks ---\n")
        for i, chunk in enumerate(all_chunks[:5]):
            print(f"[{i}] {chunk['source_file']} / {chunk['section_title']}")
            print(f"    {len(chunk['chunk_text'])} chars, index={chunk['chunk_index']}")
            preview = chunk["chunk_text"][:120].replace("\n", " ")
            print(f"    Preview: {preview}...")
            print()
        print(f"... and {len(all_chunks) - 5} more chunks")
        return

    # Database operations
    print("\nConnecting to database...")
    conn = get_db_connection()

    # Clear existing chunks for these files
    source_files = list(set(c["source_file"] for c in all_chunks))
    print(f"Clearing existing chunks for {len(source_files)} files...")
    clear_existing_chunks(conn, source_files)

    # Generate embeddings
    embeddings = None
    if not args.skip_embedding:
        print(f"\nGenerating embeddings ({EMBEDDING_MODEL})...")
        texts = [c["chunk_text"] for c in all_chunks]
        embeddings = []

        for batch_start in range(0, len(texts), args.batch_size):
            batch_end = min(batch_start + args.batch_size, len(texts))
            batch = texts[batch_start:batch_end]
            batch_embeddings = get_embeddings(batch)
            embeddings.extend(batch_embeddings)
            print(f"  Embedded {batch_end}/{len(texts)}")

    # Insert
    print(f"\nInserting {len(all_chunks)} chunks...")
    insert_chunks(conn, all_chunks, embeddings)
    conn.close()

    print("\nDone!")
    print(f"  Chunks inserted: {len(all_chunks)}")
    print(f"  Embeddings: {'yes' if embeddings else 'skipped'}")
    print(f"  Table: playbook_chunks")


if __name__ == "__main__":
    main()
