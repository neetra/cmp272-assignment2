from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from TweetsProvider import TweetProvider
from flask_cors import CORS

tp =  TweetProvider()
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

class TweetList(Resource):
    # methods go here POST and PUT
    def get(self):
      data = tp.get_tweets_from_api()
      return data, 200

class Ping(Resource):
  def get(self):
    return {'message':'Success'}, 200

class TweetSingle(Resource):
  # methods go here
    # TODO
    def get(self, id):
      data = tp.get_tweets_from_api()
      return data, 200

    def delete(self)      :
      return {'message', "deleted"}, 200

class CreateTweet(Resource):
  # methods go here
    # TODO
    def post(self, str):
      print(str);
      data = tp.post_tweet(str);
      return {'message':str}, 200


api.add_resource(Ping, '/ping')
api.add_resource(TweetList, '/tweets')
api.add_resource(TweetSingle, '/tweets/<int:id>')
api.add_resource(CreateTweet, '/tweet/post/<string:str>')

if __name__ == '__main__':
    app.run()  # run our Flask app
