import tweepy
import time


def twit_bot(consumer_key, consumer_secret, dev_key, dev_secret, search, num_tweets, like=False, retweet=False,
             cooldown=None):
    """
    A simple Twitter bot that allows for a like or retweet action to be carried out on a pre-determined number of
    search results.

    :param consumer_key: type str
        user's consumer key, available at https://developer.twitter.com/
    :param consumer_secret: type str
        user's consumer secret, available at https://developer.twitter.com/
    :param dev_key: type str
        user's developer key, available at https://developer.twitter.com/
    :param dev_secret: type str
        user's developer secret, available at https://developer.twitter.com/
    :param search: type str
        the term to be searched for
    :param num_tweets: type int
        the number of tweets to be liked and/or retweeted
    :param like: type bool
        whether search results should be liked ("favorited")
    :param retweet: type bool
        whether search results should be retweeted
    :param cooldown: type int
        if value is entered, the cool-down time (in seconds) between each search result
    :return: type None
        returns nothing
    """

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(dev_key, dev_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.me()

    print(user.screen_name)

    for tweet in tweepy.Cursor(api.search, search).items(num_tweets):
        try:
            if like:
                print("Tweet liked")
                tweet.favorite()
            if retweet:
                print("Retweeted")
                tweet.retweet()
                if cooldown:
                    time.sleep(cooldown)
        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break

    return


c_key = "YOUR_CONSUMER_KEY"
c_sec = "YOUR_CONSUMER_SECRET"
d_key = "YOUR_DEV_KEY"
d_sec = "YOUR_DEV_SECRET"


twit_bot(c_key, c_sec, d_key, d_sec, "#deeplearning", 20, like=True, retweet=True)