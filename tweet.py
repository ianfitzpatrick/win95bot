#!/usr/bin/env python

import tweepy, time, os, sys, yaml
from generate_messages import genernate_messages
from generate_image import generate_image

# Load twitter credentials for this bot from config file
BOTCRED_FILE = '%s/.botcreds' % os.path.expanduser('~') 
with open(BOTCRED_FILE, 'r') as credfile:
	bot_creds = yaml.load(credfile)

CONSUMER_KEY = bot_creds['win95bot']['consumer_key']
CONSUMER_SECRET = bot_creds['win95bot']['consumer_secret']
ACCESS_KEY = bot_creds['win95bot']['access_key']
ACCESS_SECRET = bot_creds['win95bot']['access_secret']

# Do actual authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Generate image and tweet
BOTDIR = sys.path[0]
msgs, screen = genernate_messages(BOTDIR)
img = generate_image(msgs, screen, BOTDIR)
# api.update_with_media(img)

