# Netra : Import file from server folder
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + "/server")

# Netra : test imported modules
try:
    from TweetsHandler import app
    import unittest

except Exception as e:
    print ("Some Modules are missing")

from TweetsHandler import app
import unittest
import json
import time
class FlaskTest(unittest.TestCase):

    # Netra : Test to check connectivity
    def test_ping(self):
        test = app.test_client(self)
        response = test.get("/ping")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Netra : Test to check get all tweets
    def test_get_alltweets(self):
        test = app.test_client(self)
        response = test.get("/tweets")

        # Check status code, content type, and number of tweets returns
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.get_data(as_text=True))

        # Maximum seven tweets are returned
        self.assertLessEqual(len(data), 7)

    # Zi : test post/create
    def test_post_tweet(self):
        test = app.test_client(self)
        response = test.post("/tweet/post/unittest"+str(time.time()))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

# Netra : Run the tests
if __name__ == "__main__" :
    unittest.main()
