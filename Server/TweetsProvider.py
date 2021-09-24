# Perform 'CRUD' operations on twitter API
import tweepy
import pandas as pd
from pandas.core.frame import DataFrame

#credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
token_secret = ''

class TweetProvider():
    def __init__(self):        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        self.api = tweepy.API(auth)
    
    def get_tweets(self):
        df = pd.read_json('elon_musk_Tweets.json', orient='records')       
        return df.to_json(orient = 'records')

    def get_tweets_from_api(self)        :
        public_tweets = self.api.home_timeline()        
        allTweets = [];
        for t in public_tweets:
            tweet = { 'id' : t.id, 'text' : t.text, 'author' : t.author.name }
            allTweets.append(tweet)
        return allTweets;            



