import sys
import os
import twitter
import ex8
# from ex8 import main

tapi = os.environ.get('TWITTER_API_KEY')
capi = os.environ.get('CONSUMER_SECRET')
atk = os.environ.get('ACCESS_TOKEN_KEY')
ats = os.environ.get('ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=tapi, 
    consumer_secret=capi, 
    access_token_key=atk, 
    access_token_secret=ats)

print api.VerifyCredentials()

args = sys.argv
tweet = ex8.main(args)

print tweet
user_input = raw_input("do you want to post this tweet? y/n ")
if user_input == "y":
    status = api.PostUpdate(tweet)

