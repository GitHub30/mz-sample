import os
import pickle

import tweepy

tweepy.debug(True)

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)
follower_ids = []
for follower_id in tweepy.Cursor(api.followers_ids, screen_name='yousuck2020', cursor=-1, count=5000).items():
    follower_ids.append(follower_id)

with open('follower_ids.pickle', 'wb') as f:
    pickle.dump(follower_ids, f)
