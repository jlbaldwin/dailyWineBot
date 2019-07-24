import os
import random
import requests
import json
import tweepy
import logging
import getdata
from config import *

logger = logging.getLogger()


#-------------------------------------------------------------------------------------
#create_api_obj()
#Description:
#	Create tweepy object to interact with twitter. Verify twitter credentials.
#Returns: api_obj 
#-------------------------------------------------------------------------------------
def create_api_obj():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api_obj = tweepy.API(auth)

    try:
        api_obj.verify_credentials()
    except Exception as e:
        logger.error("Error verifying credentials for API creation.", exc_info=True)
        raise e

    logger.info("API object created ok.")

    return api_obj


#-------------------------------------------------------------------------------------
#create_tweet_data()
#Description:
#	Builds Snooth GET request using a random selection of wine color and SnoothRank. 
#	The GET request returns up to 'wine_ct' number of wines, if available in the
#	Snooth API. From those wines, a single wine is randomly selected to be tweeted. 
#Returns: tweet_text => multi line text of wine info
#-------------------------------------------------------------------------------------
def create_tweet_data():
	wine_ct = 30					#number of wines to request from Snooth API

	#---------------------------------------------------------------------------------
	#constant GET components
	#---------------------------------------------------------------------------------
	address = "http://api.snooth.com/wines/"
	key = "?akey=" + SNOOTH_KEY#snooth_key 
	ip = "&ip=" + IP#ip_addr
	t = "&t=wine"					#return only wine
	n = "&n=" + str(wine_ct)		#number of results to return, default is 10 per API
	a = "&a=0"						#0 returns all wines, regardless of in stock or not
	lang = "&lang=en"


	#---------------------------------------------------------------------------------
	#variable GET components
	#---------------------------------------------------------------------------------
	color = "&color=" + random.choice(["Red", "White", "Rose"])

	rank = random.choice([2.5, 3.0, 3.5, 4.0, 4.5])
	mr = "&mr=" + str(rank)			#min ranking
	mx = "&mx="	+ str(rank + .5)	#max ranking

	req_string = address + key + ip + t + n + a + lang + mr + mx + color 

	#print("Req string to be sent:")
	#print(req_string)


	#---------------------------------------------------------------------------------
	#request data from Snooth
	#---------------------------------------------------------------------------------
	request_data = requests.get(req_string)
	response = json.loads(request_data.text)


	#---------------------------------------------------------------------------------
	#build tweet from requested data
	#---------------------------------------------------------------------------------
	#add variability to the selection by randomly choosing from the returned results
	returned_val = response['meta']['returned']
	wine_selection = random.randint(0, returned_val - 1)

	line1 = response['wines'][wine_selection]['name'] + " " + response['wines'][wine_selection]['vintage']
	line2 = "Region: " + response['wines'][wine_selection]['region']
	line3 = "Varietal: " + response['wines'][wine_selection]['varietal']
	line4 = "More info: " + response['wines'][wine_selection]['link']

	tweet_text = f'{line1}\n{line2}\n{line3}\n{line4}'

	return tweet_text