import tweepy
from tweepy.error import TweepError
from tweepy.models import ResultSet


def resolve_thread(start_tid, consumer_key, consumer_secret):
    """
    follow the current thread of replies back to the first tweet
    in the thread, and return the resulting thread of tweets

    note that the starting tweet must be a reply, as the chain is
    constructed by recursively collecting the tweet that each tweet
    is in reply to

    :param start_tid: tweet_id to start with
    :param key: twitter API consumer_key
    :param secret: twitter API consumer_secret
    :return: ResultSet of tweet objects
    """
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=5)
    if not api:
        raise TweepError('Authentication failed')
    prev_id = start_tid
    replies = ResultSet()
    while True:
        result = api.statuses_lookup([prev_id])
        prev = next(iter(result))
        replies.append(prev)
        prev_id = prev.in_reply_to_status_id
        if not prev_id:
            return replies
