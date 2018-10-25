from unittest import TestCase
from twitter_utils.replies import resolve_thread
from tweepy.error import TweepError
from twitter_utils.test import config


class TestReplies(TestCase):
    def test_thread(self):
        replies_1 = resolve_thread(1033496590965776384, config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.assertIsNotNone(replies_1)
        self.assertEqual(replies_1.ids(), [1033496590965776384, 1015777003247554560])
        replies_2 = resolve_thread(1015840934444126209, config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.assertIsNotNone(replies_2)
        self.assertEqual(replies_2.ids(),
                         [1015840934444126209, 1015840376467443713, 1015838099916644352, 1015777003247554560])
        self.assertRaises(TweepError, resolve_thread, 1033496590965776384, config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.assertRaises(TweepError, resolve_thread, 1015840934444126209, config.CONSUMER_KEY, config.CONSUMER_SECRET)
        replies_3 = resolve_thread(1054895846028963840, config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.assertIsNotNone(replies_3)
        self.assertEqual(replies_3.ids(),
                         [1054895846028963840, 1054894419562913794, 1054893130753957888, 1054887110350721026])
