twitter_utils
=============

This package currently implements one simple method: `resovle_thread`, that makes use of
[tweepy](https://github.com/tweepy/tweepy) to follow the thread of replies preceding a specified tweet
 back to the first tweet in the thread, and returns that thread.
 Creating a package for this was probably unnecessary, but I thought it would be a
 good learning experience to go through the steps to do so, and who knows - maybe I'll extend it with more functionality in future.

Installation
------------
The easiest way to install is by using pip/easy_install to pull it from PyPI.
Note that `twitter_utils` is currently only available as a test version.

    pip install --index-url https://test.pypi.org/simple/ twitter_utils

Usage
-----

`resolve_thread` returns a `ResultSet` of `Status` objects, one for each
corresponding tweet. The attributes of each `Status` may be accessed directly
and correspond to the those returned by Twitter. Read the
[Twitter docs](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html) for more info.

```
>>> from twitter_utils.replies import resolve_thread

>>> tweet_thread = resolve_thread(1054030566193065984, 'your_consumer_key', 'your_consumer_secret')
>>> print(tweet_thread.ids())

[1054030566193065984, 1054029926955995141, 1054028675044331521, 1054026646066552835, 1054022706151243776, 1054022610915352576]

>>> for x in tweet_thread:
>>>    print(x.user.screen_name+': ', x.text)

JackHubs:  @_ConnorMiles @officialjaden @DillianWhyte Preach my g preach 🙌🏻🙏🏻be humble be humble🙏🏻🙏🏻
_ConnorMiles:  @JackHubs @officialjaden @DillianWhyte https://t.co/NhmiEmQLRt
JackHubs:  @_ConnorMiles @officialjaden Lessss goo babbyyyyy
_ConnorMiles:  @JackHubs @officialjaden I’m ready when you are
JackHubs:  @officialjaden YO BRO LETS HOOK UP NOW
officialjaden:  Just Landed In London Link
```
