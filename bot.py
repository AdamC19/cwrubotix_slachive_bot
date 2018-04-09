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
	

	sep(2)
	
#	jsonObj = json.load(channels_list)
#	print(json.dumps(channels_list) )
	#for key in channels_list:
	#	print(channels_list[key])
	 
	# check if it came back OK
	if channels_list['ok'] == True:
		print('Authorization succeeded')
		
		channels = channels_list['channels']
		
		# list the keys in the channels dict
		for channel in channels:
			print("Name : " + channel['name'] )
			# for key in channel:
			# 	print("Key : " + str(key))
			

	else:
		print('Authorization failed :(')
	

#===============================================================================
if __name__ == '__main__':
	main()
