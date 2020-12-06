import tweepy
from textblob import TextBlob
import pandas as pd

# Keys and tokens
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve tweets
query = input("Search Twitter: ")
tweets = tweepy.Cursor(api.search, q = query, tweet_mode = "extended").items(10)

tweets_list = []

for tweet in tweets:
	# Sentiment analysis
	analysis = TextBlob(tweet.full_text)
	polarity = round(analysis.sentiment.polarity, 2)

	# Label the tweet's sentiment value
	sentiment = "Negative" if polarity < 0 else "Positive"

	tweets_list.append([tweet.user.screen_name, tweet.full_text, polarity, sentiment])

tweets_df = pd.DataFrame(tweets_list, columns = ["User", "Tweet", "Polarity", "Sentiment"])
tweets_df.to_csv(r"{}.csv".format(query), index = False)

print(tweets_df)