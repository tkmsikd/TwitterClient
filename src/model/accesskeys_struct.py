# AccessKeys型としてアクセス時の認証アイテムのデータを管理
import unittest


class AccessKeys:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key 
        self.consumer_secret =consumer_secret 
        self.access_token = access_token 
        self.access_token_secret = access_token_secret 


class TestAccessKeys(unittest.TestCase):
    def test_accesskeys(self):
        consumer_key = 'consumer_key'
        consumer_secret = 'consumer_secret'
        access_token = 'access_token'
        access_token_secret = 'access_token_secret'

        accesskeys = AccessKeys(consumer_key, consumer_secret, access_token, access_token_secret)
        self.assertEqual(consumer_key, accesskeys.consumer_key)
        self.assertEqual(consumer_secret, accesskeys.consumer_secret)
        self.assertEqual(access_token, accesskeys.access_token)
        self.assertEqual(access_token_secret, accesskeys.access_token_secret)

if __name__ == '__main__':
    unittest.main()
        