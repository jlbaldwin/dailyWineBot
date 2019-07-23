import tweepy
from getdata import create_api_obj, create_tweet_data


def main():
    api_obj = create_api_obj()
    tweet_text = create_tweet_data()
    api_obj.update_status(tweet_text)

    
if __name__ == "__main__":
    main()
