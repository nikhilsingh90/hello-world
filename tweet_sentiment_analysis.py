import tweepy
from textblob import TextBlob

consumer_key = "cycnpOQN42QOMbmeGwsqlTmeC"
consumer_secret = "c9wMap6GzAte5GquoXJpPHGFEB4JLfWImQZmsBEc4LvEqeBHUK"

access_token = "29011036-7qUqvimbEcuDUb5tBgmCWppRgJyPv7gLq4zS1TtCJ"
access_token_secret = "30YAq3lzlEI5U1erb0yTQdYLcPOkjU4Os0Al3IWK6aESa"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Narendra Modi")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
