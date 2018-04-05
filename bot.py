#! /usr/bin/python

from slackclient import SlackClient
from datetime import datetime
import time
import os.path
import codecs
import secrets


def main():
	token = open("slack_token.dat","r").read()

	sc = SlackClient(token)

	response = sc.api_call("api.test")
print(response)

print('*'*80)

auth_resp = sc.api_call("auth.test")
print(auth_resp)
