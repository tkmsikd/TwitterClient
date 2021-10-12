import sys
import unittest
import tweepy
sys.path.append("..")
from controller.readauthfile import ReadAuthFile
from model.accesskeys_struct import AccessKeys
#from model.utils import is_none_value_included

# 引数として、データセット済みのAccessKeys型変数を格納する
# self.api_handler を使ってAPI操作
# 使い方はTwitterAuth classをインスタンス化し、getterでapi_handlerを取得するだけ
class TwitterAuth:
    def __init__(self, accesskeys:AccessKeys):
        #if is_none_value_included(AccessKeys().__dict__):
        #    sys.exit("Given AccessKeys variable has None in its attributes")

        self._accesskeys = accesskeys
        self.api_handler = None

        self._auth_handler()

    def _auth_handler(self):
        _auth = tweepy.OAuthHandler(self._accesskeys.consumer_key, self._accesskeys.consumer_secret)
        _auth.set_access_token(self._accesskeys.access_token, self._accesskeys.access_token_secret)

        handler = tweepy.API(_auth)
        self._set_api_handler(handler=handler)

    def _set_api_handler(self, handler):
        self.api_handler = handler

    def get_api_handler(self):
        return self.api_handler

class TwitterAuthTest(unittest.TestCase):
    def test():
        return 1

if __name__ == '__main__':
    ta = TwitterAuth()