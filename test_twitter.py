# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:45:41 2020

@author: Juan Castillo
"""

import tweepy
import csv

consumer_key ='QqySEZSnUKkhHgNFJkSsXbXaF'
consumer_secret='4wD1mwlAHx20MqS8dE5vmUYs1rVKmOUoj1WN2XUItBJVXGjb68'
access_token= '1132026149700341762-pl9MPDEFZeqFFCjfUdg0C94ibYrhvV'
access_token_secret='8cT7AMfiK0RNKz5gHRwbv6HsVXIqU6pRj5ExvqeOPmqX9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#apruebo",
                        #   lang="es",
                           until ="2020-09-01").items():
    
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])