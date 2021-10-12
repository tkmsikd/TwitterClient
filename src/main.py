# !/usr/bin/env pipenv-shebang
# -*- coding: utf-8 -*-

from controller.readauthfile import ReadAuthFile
from model.accesskeys_struct import AccessKeys
from model.twitter_auth import TwitterAuth
from model.twitterhandler import TwitterHandler

if __name__ == "__main__":
    # Twitter authentication
    read_auth = ReadAuthFile()
    access_keys = AccessKeys(
        consumer_key= read_auth.get_consumer_key(),
        consumer_secret=read_auth.get_consumer_secret(),
        access_token= read_auth.get_access_token(),
        access_token_secret= read_auth.get_access_token_secret()
    )

    auth = TwitterAuth(accesskeys=access_keys)

    # Create twitter stream
    twitter_handler = TwitterHandler(auth)
    twitter_handler.fetch_tweet()