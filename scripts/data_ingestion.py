import tweepy
import os
import configparser

def authenticator():
    # parse the credentials from auth.txt
    config_dir = os.path.join("scripts","auth.txt")

    config = configparser.ConfigParser()
    config.read(config_dir)

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

def ingest_data(start_year=2011, end_year=2017):

    api_object = authenticator()

    # this is methodic because we don't really scrap the web due to api interference issues.
    top_tweeters = [
        "BarackObama", "justinbieber", "katyperry", "rihanna", "realDonaldTrump",
        "ladygaga", "TheEllenShow", "Cristiano", "YouTube", "jtimberlake",
        "KimKardashian", "britneyspears", "Oprah", "ArianaGrande", "selenagomez",
        "Twitter", "taylorswift13", "BillGates", "narendramodi", "shakira"
    ]

    # initialize a dictionary to store tweets of each tweeter
    tweets_dict = {
        "author": [],
        "content": [],
        "country": [],
        "date_time": [],
        "language": [],
        "latitude": [],
        "longitude": [],
        "number_of_likes": [],
        "number_of_shares": []
    }

    for tweeter in top_tweeters:
        try:
            # Paginate through the user timeline to retrieve tweets
            for tweet in tweepy.Cursor(api_object.user_timeline, user_id=tweeter).items():
                if tweet.created_at.year == end_year:
                    tweets_dict["author"].append(tweet.author.username)
                    tweets_dict["content"].append(tweet.text)
                    tweets_dict["country"].append(tweet.place.country if tweet.place else None)
                    tweets_dict["date_time"].append(tweet.created_at)
                    tweets_dict["language"].append(tweet.lang)
                    tweets_dict["latitude"].append(tweet.geo.coordinates[0] if tweet.geo else None)
                    tweets_dict["longitude"].append(tweet.geo.coordinates[1] if tweet.geo else None)
                    tweets_dict["number_of_likes"].append(tweet.favorite_count)
                    tweets_dict["number_of_shares"].append(tweet.retweet_count)
        except Exception as e:
            print(f"Error retrieving tweets for {tweeter}: {e}")
            pass
    print("\n *** \nBecause problem in interfacing with twitter API v1 and v2, we will use the toy dataset of kaggle\n *** \n")

    # create DataFrame from the collected tweets - because the API problems we don't actually run this line
    # tweets_df = pd.DataFrame(tweets_dict)
    # instaed we load the kagle datasheet
    # return pd.read_csv(os.path.join("..", 'data','tweets_df.csv'))

if __name__ == "__main__":
    authenticator()
    ingest_data()