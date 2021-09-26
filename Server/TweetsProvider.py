# Netra : Import tweepy to handle twitter API
import tweepy

#Netra : Initialize the credentials to access API 
#credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
token_secret = ''

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



