import tweepy
import time


def twit_bot(consumer_key, consumer_secret, dev_key, dev_secret, search, num_tweets, like=False, retweet=False,
             cooldown=None):

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