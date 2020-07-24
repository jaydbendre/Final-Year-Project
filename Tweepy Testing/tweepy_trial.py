import tweepy
import pandas as pd

consumer_key = "4cHuVVUX1PCBd5NSRLPrQIdt1"
consumer_secret = "Zb7d1f5PDQKk7p3LqXzP1hcabrbPm2aVR17glNZceYe5D2kfg2"
access_token = "2308761914-WXsoRl3Rj75v0ipaoJRL4Wv6Z4T3jaAgN7EwtLp"
access_secret = "dsjAD1wSsF1AnRGolwYqkLDG6YrEnrs149odgwl7rlL0r"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []
for tweet in tweepy.Cursor(api.search, q="#blm", count=10, lang="en", since="2020-01-01").items():
    tweets.append(
        {
            "created_at": tweet.created_at,
            "text": tweet.text.encode("utf-8"),
            "user_id": tweet.user.id,
            "user_name": tweet.user.screen_name,
            "location": tweet.user.location,
        }
    )
    if len(tweets) == 5000:
        break

df = pd.DataFrame(tweets)
df.to_csv("TestFile.csv")
