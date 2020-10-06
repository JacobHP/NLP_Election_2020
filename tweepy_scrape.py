#twitter developer account needed to run script
import tweepy
import pandas as pd
from datetime import datetime as dt
from ratelimit import limits, sleep_and_retry
consumer_key=str(input('Consumer key: '))
consumer_secret=str(input('Consumer secret: '))
access_key=str(input('Access key: '))
access_secret=str(input('Access secret: '))

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


api=tweepy.API(auth)

wait=900  
calls=15 
@sleep_and_retry
@limits(calls=calls, period=wait)
def get_tweets(query, language, date_since=dt.today().date(), maxItems=None):
    tweets_list=[]

    try:
        tweets=tweepy.Cursor(api.search, q=query, lang=language, since=date_since, extended=True,tweet_mode='extended').items(maxItems)
    except Exception as e:
        print('Error: '+str(e))

    for tweet in tweets:
        tweet_atts=[]
        tweet_atts.append(tweet.full_text)
        tweet_atts.append(tweet.favorite_count)
        tweet_atts.append(tweet.retweet_count)
        tweet_atts.append(tweet.user.name)
        tweet_atts.append(tweet.user.location)
        tweet_atts.append(tweet.user.followers_count)
        tweet_atts.append(tweet.user.created_at)
        tweet_atts.append(tweet.created_at)
        tweet_atts.append(tweet.entities['hashtags'])
        tweet_atts.append(tweet.entities['user_mentions'])
        tweet_atts.append(tweet.entities['urls'])
        tweets_list.append(tweet_atts)
    return tweets_list


test=get_tweets(query='US Election',language='en',maxItems=10000)

tweets_df=pd.DataFrame(test,columns=['contents','likes','retweets','username','location','followers','user_create', 'tweet_create','hashtag','mentions', 'urls'])
tweets_df.to_csv('Election_tweets_'+str(dt.today().date())+'.csv')

