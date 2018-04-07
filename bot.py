#! /usr/bin/python

from slackclient import SlackClient
from datetime import datetime
import time
import os.path
import codecs
import secrets
import json

#===============================================================================
def sep(n):
	for i in range(0,n):
		print('*'*80)
#===============================================================================
def main():
	token = open("slack_token.dat","r").read()

	sc = SlackClient(token)

	#response  		= sc.api_call("api.test")
	#auth_resp 		= sc.api_call("auth.test")
	channels_list 	= sc.api_call("channels.list")
	history   		= sc.api_call("channels.history")

	#sep(2)
	#print(response)
	#sep(2)
	#print(auth_resp)
	#sep(2)
	#channelsJSON = channels_list.encode('utf_8', 'strict')
	#print(channels_list)
	sep(2)
#	print(history)
#	sep(2)

	#json.loads(channels_list)
	print(json.dumps(channels_list) )
	#for key in channels_list:
	#	print(channels_list[key])

#===============================================================================
if __name__ == '__main__':
	main()
