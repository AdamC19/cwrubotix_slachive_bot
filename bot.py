#! /usr/bin/python

from slackclient import SlackClient
from datetime import datetime
import time
import os.path
import codecs

token = open("slack_token.dat","r").read()

sc = SlackClient(token)

response = sc.api_call("auth.test");
print(response)
