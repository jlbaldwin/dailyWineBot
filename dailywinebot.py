import tweepy
import logging
import os

logger = logging.getLogger()

def create_api_obj():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api_obj = tweepy.API(auth)

    try:
        api_obj.verify_credentials()
    except Exception as e:
        logger.error("Error creating API.", exc_info=True)
        raise e

    logger.info("API created ok.")
    return api_obj

def main():
    api_obj = create_api_obj()
    api_obj.update_status("Hello, world...of wine.")

    
if __name__ == "__main__":
    main()
