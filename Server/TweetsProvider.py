# Perform 'CRUD' operations on twitter API
import tweepy
import pandas as pd
from pandas.core.frame import DataFrame

#credentials
consumer_key = "Eb3fSiF7rMZiv0CrtpHms9yOW"
consumer_secret = "pGkE3xGXAh6w3i2odQ3YOnsng9QKKZ7TBY8aKcVHRLFz0V1oYO"
access_token = "1434974690703908864-0hJrYAZoqUFPZAXlRBPckWlQJbhkOY"
token_secret = "8P5CDkA7jUkXsHWlQEWMH1MXNeHevXwthM4gYZu0QFpgH"

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

    def post_tweet(self, status):
        df = self.api.update_status(status);
        return df;
