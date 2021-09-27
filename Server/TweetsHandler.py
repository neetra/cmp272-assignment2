from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from TweetsProvider import TweetProvider
from flask_cors import CORS

# Netra : Create instance of provider class, Handle Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible, instantiate Flask to create REST API
tp =  TweetProvider()
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

#Netra : Create endpoints
class TweetList(Resource):

    # Netra: Get tweets
    def get(self):
      data = tp.get_tweets_from_api()
      return data, 200

# Netra : Check connectivity
class Ping(Resource):
  def get(self):
    return {'message':'Success'}, 200

# Zi : Create the tweet
class CreateTweet(Resource):
  # methods go here
    def post(self, str):
      print(str);
      data = tp.post_tweet(str);
      return {'message':str}, 200

# Govinder/Rohan : Delete the tweet
class DeleteTweet(Resource):
  def delete(self, status_id):
    print(status_id+" to be deleted ...");
    data = tp.del_tweet(status_id);
    return {'message' : status_id}, 200


# Netra
api.add_resource(Ping, '/ping')
api.add_resource(TweetList, '/tweets')

# Zi
api.add_resource(CreateTweet, '/tweet/post/<string:str>')

# Govinder
api.add_resource(DeleteTweet, '/tweet/delete/<string:status_id>')

# Netra: Run flask app
if __name__ == '__main__':
    app.run()
