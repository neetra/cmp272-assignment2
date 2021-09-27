# Netra : Import tweepy to handle twitter API
import tweepy

#credentials : Initilaize credentials 
consumer_key = "Eb3fSiF7rMZiv0CrtpHms9yOW"
consumer_secret = "pGkE3xGXAh6w3i2odQ3YOnsng9QKKZ7TBY8aKcVHRLFz0V1oYO"
access_token = "1434974690703908864-0hJrYAZoqUFPZAXlRBPckWlQJbhkOY"
token_secret = "8P5CDkA7jUkXsHWlQEWMH1MXNeHevXwthM4gYZu0QFpgH"

# Netra : Create class to handle twitter API
class TweetProvider():

    #Netra : Authtenticate tweepy and create object for API class
    def __init__(self):        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        self.api = tweepy.API(auth)     

    # Netra : Get recent Tweets and Retweets posted by the authenticating user and the users they follow.
    def get_tweets_from_api(self)        :
        public_tweets = self.api.home_timeline(count = 5) 
        user_tweets = self.api.user_timeline(count = 2) 
        public_tweets = public_tweets + user_tweets
        allTweets = [];
        for t in public_tweets:
            tweet = { 'id' : t.id, 'text' : t.text, 'author' : t.author.name }
            allTweets.append(tweet)
        return allTweets;

    # Zi : Create a tweet
    def post_tweet(self, status):
        df = self.api.update_status(status);
        return df;   
    
    # Govinder/Rohan : Create a tweet
    def del_tweet(self, status):
        df = self.api.destroystatus(self, status);
        return df;
        



