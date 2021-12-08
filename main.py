import tweepy
from dotenv import load_dotenv, dotenv_values

load_dotenv()

config = dotenv_values(".env")

CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_SECRET = config["CONSUMER_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = config["ACCESS_TOKEN_SECRET"]
BEARER_TOKEN = config["BEARER_TOKEN"]

SCREEN_NAME = config["SCREEN_NAME"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)


class StreamListener(tweepy.Stream):
    def on_connect(self):
        print("Connected to the Twitter stream")

    def on_status(self, tweet):
        if hasattr(tweet, "quoted_status"):
            if tweet.quoted_status.user.screen_name == SCREEN_NAME:
                if not tweet.favorited:
                    client.like(tweet.id)


stream_listener = StreamListener(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
stream_listener.filter(track=[SCREEN_NAME])
