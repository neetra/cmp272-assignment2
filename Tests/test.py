import sys
import time
sys.path.append('../server')
try:
    from TweetsHandler import app
    import unittest

except Exception as e:
    print ("Some Modules are missing")

from TweetsHandler import app
import unittest
class FlaskTest(unittest.TestCase):

    #check self test
    def test_ping(self):
        test = app.test_client(self)
        response = test.get("/ping")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_alltweets(self):
        test = app.test_client(self)
        response = test.get("/tweets")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # # TODO
    def test_get_singletweet(self):
        test = app.test_client(self)
        response = test.get("/tweets/9")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test post/create
    def test_post_tweet(self):
        test = app.test_client(self)
        response = test.post("/tweet/post/unittest"+str(time.time()))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)



if __name__ == "__main__" :
    unittest.main()
