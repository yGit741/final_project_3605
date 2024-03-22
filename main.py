import os
import configparser

from microservices.auth import authenticator
from microservices.twitter_scarper import scrap_top_twitter_in_range

auth_dir = os.path.join("data", "auth.txt")
config = configparser.ConfigParser()
config.read(auth_dir)

if __name__ == "__main__":
    api = authenticator(config)
    df = scrap_top_twitter_in_range(api, 2011, 2017)
    print(df)


