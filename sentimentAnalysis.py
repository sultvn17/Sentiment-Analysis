import tweepy 
from textblob import TextBlob

#initialize login credentials 
consumer_key = '30vWAAS1pbcjDfH9HXfg7A1t8'
consumer_secret = 'tY04S2P5Y17UePcgFoz2zPuEdG40MTgdGAitPdkDFgdOrcxWtp'

access_token = '814145635-L3w4pTs6QEPgT12xgZ2iVqT0PRsKkCfBfxsrzQ8p'
access_token_secret = 'inNnVYh5hs4mvKWq8zO9pHzjjfPeeAGCX2VdmDJet4dol'

#authenticate login credentials
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# use credentials to login with API
api = tweepy.API(auth)

# find tweets based on the keyword 
public_tweets = api.search('hip hop')

#display tweets and its sentiment analysis 
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)
	# determine how the person feels based on tweet
	if analysis.sentiment.polarity < 0:
		print('upset')
	else:
		print('happy')
