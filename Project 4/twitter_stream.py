import tweepy
import cnfg
import time
import json
from pymongo import MongoClient
import pymongo
from tqdm import tqdm



#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420 :
            #returning False in on_data disconnects the stream
            return False
    
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print('\nRateLimitError.....sleeping....zzzzzzzzz.......\n')
            for i in tqdm(range(60)):
                time.sleep(5)
        except tweepy.TweepError as e:
            if e.message.split()[-1] == '429':
                print('\nTweepError 429....sleeping...zzzzzzzzz......\n')
                for i in tqdm(range(60)):
                    time.sleep(5)

                #print('\nTweepError 429....sleeping...zzzzzzzzz......\n')
                #time.sleep(15 * 60)
            else:
                print(e.message)

if __name__ == '__main__':


    config = cnfg.load(".twitter_config")
    
    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])


    # auth = tweepy.AppAuthHandler(config["consumer_key"], config["consumer_secret"])
    api = tweepy.API(auth) #, wait_on_rate_limit=True,
                   #wait_on_rate_limit_notify=True)

    client = pymongo.MongoClient()
    db = client.climatechange
    col = db.climate_tweets_stream



tweetCount = 0
print('Streaming tweets.')

#try:

for tweet in limit_handled(tweepy.Cursor(api.search, q ='#climatechange OR climate change OR #globalwarming OR global warming' , tweet_mode = 'extended').items()):
    col.insert(tweet._json)

    tweetCount += 1
    print(tweetCount)

#except tweepy.TweepError as e:
    # Just exit if any error
    #print("some error : " + str(e))




print ("Downloaded {0} tweets, Saved to MongoDB ClimateChange".format(tweetCount))