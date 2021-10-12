import yaml
import unittest
import sys
import unittest

AUTH_FILE = "auth.yaml"

class ReadAuthFile:
    def __init__(self) -> None:
       auth:str = "../" + AUTH_FILE
       self.file = open(auth, 'rb') 
       self.consumer_key = yaml.safe_load(self.file)
    
    def __del__(self):
        print('ReadAuthFile Destructed')

    def get_bearer_token(self) -> str:
       print('get_bearer_token')
       return self.consumer_key['authentication']['bearer_token']

    def get_consumer_key(self) -> str:
       return self.consumer_key['authentication']['consumer_key']

    def get_consumer_secret(self) -> str:
       return self.consumer_key['authentication']['consumer_secret']

    def get_access_token(self) -> str:
       return self.consumer_key['authentication']['access_token']

    def get_access_token_secret(self) -> str:
       return self.consumer_key['authentication']['access_token_secret']


class TestReadAuthFile(unittest.TestCase):
    def test_get_bearer_token(self):
       read_auth = ReadAuthFile()
       actual = read_auth.get_bearer_token()
       expected = ""
       self.assertEqual(expected, actual)

    def test_get_consumer_key(self):
       read_auth = ReadAuthFile()
       actual = read_auth.get_consumer_key()
       expected = ""
       self.assertEqual(expected, actual)

    def test_get_consumer_secret(self):
       read_auth = ReadAuthFile()
       actual = read_auth.get_consumer_secret()
       expected = ""
       self.assertEqual(expected, actual)

    def test_get_access_token(self):
       read_auth = ReadAuthFile()
       actual = read_auth.get_access_token()
       expected = ""
       self.assertEqual(expected, actual)

    def test_get_access_token_secret(self):
       read_auth = ReadAuthFile()
       actual = read_auth.get_access_token_secret()
       expected = ""
       self.assertEqual(expected, actual)

if __name__ == "__main__":
   unittest.main()