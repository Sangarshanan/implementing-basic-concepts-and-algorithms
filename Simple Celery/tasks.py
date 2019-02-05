from celery import Celery
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
from celery.decorators import periodic_task


app = Celery()

@periodic_task(run_every=timedelta(seconds=5))
def latest_tweet():
	website_url = requests.get('https://twitter.com/Twitter').text
	soup = BeautifulSoup(website_url,'lxml')
	first_tweet = soup.find('p',{'class':'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}).text
	return (first_tweet)
