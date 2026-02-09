#!/usr/bin/env python3
"""
ArchivlyX Twitter Likes 스크래퍼
자동으로 수집하여 CSV와 Markdown 파일로 저장합니다.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import re
import logging
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("scraper.log", encoding='utf-8', mode='w'),
        logging.StreamHandler()
    ]
)

def setup_driver():
    r"""
    실행 중인 Chrome 브라우저에 연결합니다.
    """
    options = webdriver.ChromeOptions()
    # 실행 중인 Chrome 위치 지정 (버전 불일치 방지용)
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # 이미 실행 중인 크롬의 디버깅 포트에 연결
    # 로그 분석 결과: IPv4(127.0.0.1)는 다른 프로세스(좀비)가 점유 중이고, 
    # 현재 사용 중인 창은 IPv6([::1])에 바인딩되었습니다.
    options.add_experimental_option("debuggerAddress", "[::1]:9222")
    
    # 드라이버 서비스 설정
    try:
        # 1. 자동 설치 시도
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        logging.warning(f"Managed Driver 연결 실패 ({e}), 시스템 기본 드라이버로 재시도합니다.")
        try:
            # 2. 기본 드라이버 시도 (PATH에 있는 경우)
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception as e2:
            logging.error(f"최종 연결 실패: {e2}")
            raise e2

def wait_for_page_load(driver):
    """페이지 로딩 대기"""
    try:
        # ArchivlyX의 카드 요소 대기
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-slot="card"]'))
        )
        time.sleep(2)
        return True
    except TimeoutException:
        current_url = driver.current_url
        logging.error(f"페이지 로드 타임아웃. 현재 URL: {current_url}")
        return False

def extract_posts_from_page(driver):
    """현재 페이지에서 모든 포스트 추출"""
    posts = []
    
    try:
        # 1. ArchivlyX 카드 요소 찾기
        cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-slot="card"]')
        
        logging.info(f"카드 요소 {len(cards)}개 발견.")
        
        if not cards:
             logging.warning("카드를 찾지 못했습니다.")
             return []

        for card in cards:
            try:
                post_data = extract_post_from_card(card)
                if post_data:
                    posts.append(post_data)
            except Exception as e:
                # logging.warning(f"카드 추출 중 오류: {e}") 
                continue

    except Exception as e:
        logging.error(f"데이터 추출 중 치명적 오류: {e}")
    
    return posts

def extract_post_from_card(card):
    """개별 카드에서 정보 추출"""
    try:
        card_text_all = card.text
        
        # 기본값
        username = "Unknown"
        nickname = ""
        post_date = "Unknown"
        post_text = ""
        link = ""

        # 1. 닉네임 (font-semibold)
        try:
            nickname = card.find_element(By.CSS_SELECTOR, "span.font-semibold.text-sm").text
        except:
            pass

        # 2. 핸들 (@username) & 날짜
        # text-muted-foreground 클래스를 가진 span들을 순회
        try:
            meta_spans = card.find_elements(By.CSS_SELECTOR, "span.text-muted-foreground.text-sm")
            for span in meta_spans:
                txt = span.text.strip()
                if txt.startswith("@"):
                    username = txt.lstrip("@")
                elif re.search(r'(ago|year|month|day|hour|minute)', txt, re.IGNORECASE):
                    post_date = txt
        except:
            pass
            
        # fallback: 정규식으로 찾기
        if username == "Unknown":
            user_match = re.search(r'(@[a-zA-Z0-9_]+)', card_text_all)
            if user_match:
                username = user_match.group(1).lstrip('@')

        # 3. 포스트 텍스트
        try:
            text_elem = card.find_element(By.CSS_SELECTOR, "p.text-sm.leading-relaxed")
            post_text = text_elem.text
        except:
            pass
            
        # 4. 링크 추출
        # 카드 내의 링크 탐색
        try:
            links = card.find_elements(By.TAG_NAME, "a")
            for l in links:
                href = l.get_attribute("href")
                if href and ("t.co" in href or "x.com" in href or "twitter.com" in href):
                    link = href
                    break
            # 텍스트 내의 링크일 수도 있음
            if not link:
                url_match = re.search(r'(https?://t\.co/[a-zA-Z0-9]+)', post_text)
                if url_match:
                    link = url_match.group(1)
        except:
            pass
            
        # 데이터가 너무 부실하면 제외
        if username == "Unknown" and not post_text:
            return None
            
        return {
            'username': username,
            'nickname': nickname,
            'post_date': post_date,
            'post_text': post_text,
            'link': link
        }
    except Exception as e:
        return None

def attempt_next_page(driver):
    """다음 페이지 이동 (버전 6: JavaScript 기반 탐색)"""
    try:
        # 현재 페이지 위치 파악
        page_info = "Unknown"
        try:
            # "Page X of Y" 텍스트가 포함된 모든 요소 탐색
            page_info_elem = driver.execute_script("""
                return Array.from(document.querySelectorAll('div, span'))
                    .find(el => el.textContent.includes('Page') && el.textContent.includes('of'));
            """)
            if page_info_elem:
                page_info = page_info_elem.text
                logging.info(f"현재 UI 표시 상태: {page_info}")
        except:
            pass

        # JavaScript를 사용하여 '다음(>)' 버튼 찾기
        # lucide-chevron-right 아이콘을 가지고 있으며, lucide-chevrons-right(맨끝)는 아닌 버튼
        find_btn_script = """
            return (function() {
                const buttons = Array.from(document.querySelectorAll('button'));
                for (let btn of buttons) {
                    const svg = btn.querySelector('svg');
                    if (!svg) continue;
                    
                    const cls = svg.getAttribute('class') || '';
                    // 'chevron-right' 가 포함되되 'chevrons'는 아닌 것
                    if (cls.includes('lucide-chevron-right') && !cls.includes('lucide-chevrons-right')) {
                        // 비활성화 상태가 아니어야 함
                        const isDisabled = btn.disabled || btn.getAttribute('disabled') !== null || btn.classList.contains('disabled');
                        if (!isDisabled) {
                            return btn;
                        }
                    }
                }
                return null;
            })();
        """
        
        next_btn = driver.execute_script(find_btn_script)

        if next_btn:
            logging.info("클릭 가능한 '다음(>)' 버튼을 발견했습니다.")
            # 클릭 전 요소 확보
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
            time.sleep(1)
            # 직접 클릭
            driver.execute_script("arguments[0].click();", next_btn)
            
            # 페이지 전환 및 데이터 로딩 충분히 대기
            logging.info("버튼 클릭 완료, 다음 페이지 로딩 대기 중 (4초)...")
            time.sleep(4)
            return True
        else:
            # 버튼을 못 찾은 경우 상세 분석 로그
            logging.warning("클릭 가능한 '다음' 버튼을 찾지 못했습니다.")
            return False

    except Exception as e:
        logging.error(f"페이지 이동 중 오류 발생: {e}")
        return False

def scrape_all_pages(driver, start_url):
    """모든 페이지를 스크래핑 (페이지네이션 대응)"""
    all_posts = []
    
    if start_url not in driver.current_url:
        print(f"이동 중: {start_url}")
        driver.get(start_url)
    
    logging.info(f"현재 페이지: {driver.current_url}")
    logging.info("스크래핑을 시작합니다...")
    
    page_num = 1
    
    # 중복 방지를 위한 Set (고유 ID 또는 링크 기준)
    collected_hashes = set()

    while True:
        logging.info(f"[{page_num}] 페이지 데이터 추출 중...")
        
        if not wait_for_page_load(driver):
             logging.warning("페이지 로딩이 지연되고 있습니다. 시도 가능한 범위까지 추출합니다.")

        # 현재 페이지의 모든 카드 추출
        current_posts = extract_posts_from_page(driver)
        
        new_items_count = 0
        for post in current_posts:
            # 링크가 있으면 링크를 기준, 없으면 텍스트 앞부분으로 고유 키 생성
            unique_key = post['link'] if post['link'] else f"{post['username']}_{post['post_text'][:30]}"
            if unique_key and unique_key not in collected_hashes:
                collected_hashes.add(unique_key)
                all_posts.append(post)
                new_items_count += 1
        
        logging.info(f"✓ {page_num}페이지에서 {new_items_count}개 신규 수집 (총 누적: {len(all_posts)}개)")
        
        # 다음 페이지 버튼 클릭 시도
        if not attempt_next_page(driver):
            logging.info("더 이상 이동할 페이지가 없어 종료합니다.")
            break
            
        page_num += 1
        if page_num > 1000: # 무한 루프 방지
            break
    
    return all_posts

def save_to_csv(posts, filename='twitter_likes_archivlyx.csv'):
    """CSV 파일로 저장"""
    if not posts:
        return None
    df = pd.DataFrame(posts)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    logging.info(f"CSV 파일 저장 완료: {filename}")
    return df

def save_to_markdown(posts, filename='twitter_likes_archivlyx.md'):
    """Markdown 파일로 저장"""
    if not posts:
        return
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Twitter Likes - ArchivlyX\n\n")
        f.write(f"수집 날짜: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"총 포스트 수: {len(posts)}\n\n")
        f.write("---\n\n")
        
        for i, post in enumerate(posts, 1):
            f.write(f"## {i}. @{post['username']} ({post.get('nickname','')})\n\n")
            f.write(f"**날짜:** {post['post_date']}\n\n")
            f.write(f"{post['post_text']}\n\n")
            if post['link']:
                f.write(f"**링크:** {post['link']}\n\n")
            f.write("---\n\n")
    
    logging.info(f"Markdown 파일 저장 완료: {filename}")

def main():
    """메인 함수"""
    print("="*60)
    print("ArchivlyX Twitter Likes 스크래퍼 (Fixed Selectors)")
    print("="*60)
    
    start_url = "https://www.archivlyx.com/twitter-vault/likes"
    driver = setup_driver()
    
    try:
        all_posts = scrape_all_pages(driver, start_url)
        
        print(f"\n{'='*60}")
        print(f"스크래핑 완료! 총 {len(all_posts)}개 포스트 수집")
        print(f"{'='*60}")
        
        if all_posts:
            save_to_csv(all_posts)
            save_to_markdown(all_posts)
        else:
             print("수집된 데이터가 없습니다. 로그를 확인하세요.")
            
    except Exception as e:
        logging.error(f"오류 발생: {e}")
        print(f"\n❌ 오류 발생: {e}")
    finally:
        driver.quit()
        print("\n✓ 브라우저 종료")

if __name__ == "__main__":
    main()
