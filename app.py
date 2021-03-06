import tweepy
import time

auth = tweepy.OAuthHandler('api_key','api_key_secret')
auth.set_access_token('access_token','access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search  = 'python'
tweets = 100
for tweet in tweepy.Cursor(api.search, search).items(tweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break