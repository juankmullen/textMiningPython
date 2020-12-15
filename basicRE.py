# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

texto = 'To \n be or not to be'

token = texto.split(' ')

test = [w for w in token if w.istitle()]
end = [w for w in token if w.endswith('o')]

test =' Jua n. '

print(test.isalnum())

split = texto.splitlines()

strip = test.replacestrip()



#%% RE
import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.", 
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]

df = pd.DataFrame(time_sentences, columns=['text'])

#%% find the number of characters for each string in df['text']
print(df['text'].str.len())

#%% find the number of tokens for each string in df['text']
print(df['text'].str.split().str.len())

#%% find which entries contain the word 'appointment'
df['text'].str.contains('appointment')

#%% find how many times a digit occurs in each string
print(df['text'].str.count(r'\d'))

#%% find all occurances of the digits
print(df['text'].str.findall(r'\d'))

#%% group and find the hours and minutes
print(df['text'].str.findall(r'(\d?\d):(\d\d)'))

#%% replace weekdays with '???'
print(df['text'].str.replace(r'\w+day\b', '???'))

#%% replace weekdays with 3 letter abbrevations
print(df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3]))

#%% create new columns from first match of extracted groups
extract =df['text'].str.extract(r'(\d?\d):(\d\d)')
