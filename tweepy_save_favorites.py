import tweepy
import sys
from datetime import datetime, timedelta
# Consumer keys and access tokens, used for OAuth
consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'
access_token = 'xxxxx'
access_token_secret = 'xxxxx'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
user = api.me()
fdate=datetime.utcnow()-timedelta(days=365)
tdate=datetime.utcnow()-timedelta(days=100)
f = open("favorite.txt", 'a')  

for n in range(30, 50):
	favorites=api.favorites(page=n)
	n=n+1
	for obj in favorites: 
		if obj.created_at>=fdate and obj.created_at<=tdate:
			f.write(obj.created_at.strftime("%y-%m-%d %H:%M:%S")+ " " + obj.user.screen_name.encode("utf-8") + " "+ obj.text.encode("utf-8"));
			f.write("\n\n")
		else:
			f.write("no!")
			f.write("\n\n")
f.close()  