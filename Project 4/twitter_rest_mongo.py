import cnfg
import tweepy
import json
from pymongo import MongoClient
import pymongo


client = pymongo.MongoClient("mongodb://emilygeller:p@54.173.47.58:27017/climatechange")
db = client.climatechange
col = db.climate_tweets





config = cnfg.load(".twitter_config")

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(config["consumer_key"], config["consumer_secret"])


api = tweepy.API(auth, wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code

import sys
import jsonpickle
import os

searchQuery = ('#climatechange OR climate change OR #globalwarming OR global warming')  # this is what we're searching for
maxTweets = 500000 # Some arbitrary large number
tweetsPerQry = 450  # this is the max the API permits
language = 'en' # only get tweets in english
tweetmode = 'extended'
#fName = 'tweets.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = 1e4000

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

while tweetCount < maxTweets:
    try:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang= language, tweet_mode = tweetmode)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId, lang= language, tweet_mode = tweetmode)
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1), lang= language, tweet_mode = tweetmode)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId, lang= language, tweet_mode = tweetmode)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            #jsondata = json.dumps(tweet._json)
            col.insert(tweet._json)
        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        break

print ("Downloaded {0} tweets, Saved to MongoDB ClimateChange".format(tweetCount))