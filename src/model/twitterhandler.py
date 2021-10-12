import tweepy
from enum import Enum

from model.twitter_auth import TwitterAuth

class FetchDataType(Enum):
    TWEET = None # 'get' or 'set'
    USERDATA = None # if TWEET='set', user id of myself. if TWEET='get', user id of someone you want

class TwitterHandler:
    def __init__(self, auth: TwitterAuth) -> None:
        self._api_handler = auth.get_api_handler()

    def fetch_tweet(self):
        public_tweets = self._api_handler.home_timeline()
        for tweet in public_tweets:
            print(tweet)