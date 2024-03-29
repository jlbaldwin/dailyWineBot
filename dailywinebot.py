import tweepy
from getdata import create_api_obj, create_tweet_data

#-------------------------------------------------------------------------------------
#Create tweepy api object to interact with twitter. create_tweet_data hits Snooth API
#   to create tweet content. update_status sends tweet.
#-------------------------------------------------------------------------------------
def main():
	api_obj = create_api_obj()
	tweet_text = create_tweet_data()
	api_obj.update_status(tweet_text)


if __name__ == "__main__":
	main()
