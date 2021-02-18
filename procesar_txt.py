# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:50:50 2021

@author: Juan Carlos Castillo
"""

#%% Librerias
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.data import load
from nltk.stem import SnowballStemmer
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

import spacy
nlp = spacy.load('es_core_news_sm')

spanish_stopwords = stopwords.words('spanish')
stemmer = SnowballStemmer('spanish')
non_words = list(punctuation)



#%%carga de data 

file = 'gonzalo_text.csv'
gonzalo_data =pd.read_csv(file,delimiter=';')

#%% Limpieza palabra

text = 'Soy un texto que pide a gritos que lo procesen. Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan…'
doc = nlp(text)
lemmas = [tok.lemma_.lower() for tok in doc]
#%% Recorrido
vectorizer = CountVectorizer(
                analyzer = 'word',                
                lowercase = True,
                stop_words = spanish_stopwords)

vectorizer.fit_transform(gonzalo_data.tweet.dropna())

