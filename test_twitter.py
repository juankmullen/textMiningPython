# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:45:41 2020

@author: Juan Castillo
"""
# -*- coding: utf-8 -*-
import tweepy
import csv
import pandas as pd


consumer_key ='QqySEZSnUKkhHgNFJkSsXbXaF'
consumer_secret='4wD1mwlAHx20MqS8dE5vmUYs1rVKmOUoj1WN2XUItBJVXGjb68'
access_token= '1132026149700341762-pl9MPDEFZeqFFCjfUdg0C94ibYrhvV'
access_token_secret='8cT7AMfiK0RNKz5gHRwbv6HsVXIqU6pRj5ExvqeOPmqX9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('gonzalo.csv', 'w',encoding="utf-8")
#Use csv Writer
csvWriter = csv.writer(csvFile,delimiter=';')

cont = 0
cant_item= 100
cols = ['fecha','autor','tweet']

lst = []


for tweet in tweepy.Cursor(api.search,q="@carreragonzalo",
                           exclude_replies=True,
                           until ="2021-02-18").items():         
    
    lst.append([tweet.created_at,tweet.user.screen_name,tweet.text])
    cont += 1

df = pd.DataFrame(data=lst,columns = cols)
df.to_csv('gonzalo_text.csv',index=False,sep=';')
