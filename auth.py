import configparser
import tweepy


def authenticator(auth_file_dir):

    config = configparser.ConfigParser()
    config.read(auth_file_dir)

    # read credentials from the config object
    consumer_key = config.get("credentials", "consumer_key")
    consumer_secret = config.get("credentials", "consumer_secret")
    access_token = config.get("credentials", "access_token")
    access_token_secret = config.get("credentials", "access_token_secret")

    # authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print(f"A valid API object created: '{api}'")
    return api


if __name__ == '__main__':
    authenticator("auth.txt")