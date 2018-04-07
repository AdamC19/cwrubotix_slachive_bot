# cwrubotix_slachive_bot
A workaround for slack's free account storage limit
======
## Description
This is a bot that will save messages from the CWRUbotix slack channel and make them available for later, so that we can archive more than 10,000 messages because the premium slack is hella expensive.

## Setting up the Slack App
### Relevant Documentation
* [Slack API](https://api.slack.com/)
* [Python SlackClient](https://pypi.python.org/pypi/slackclient)

### Required Scopes
* ```channels:history```
   Access user’s public channels
* ```channels:read```
   Access information about user’s public channels
* ```chat:write:bot```
   Send messages as archive
* ```team:read```
   Access information about your workspace


## About the Name
"slachive" is a portmanteau of "slack" and "archive."
