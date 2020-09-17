# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# %%    Importacion de bliblioteca y datos
import pandas as pd
import nltk

data  = pd.read_csv('licitacionesheader.csv',sep=';')
# %%    Creacion Variables
data = data[data.nm_estado == 'Publicada']
descripcion = data['descripcion'].values.tolist()
# %%  Tokenizacion
from nltk.corpus import stopwords
import re

stop_words = stopwords.words('spanish');

doc = [item for item in descripcion ]

doc_token = [nltk.word_tokenize(item.lower()) for item in descripcion]
nodo_filtrado =[]
doc_tokens_clean=[];
text_clean = [];
doc_clean = [];
bolsa_clean=''

for i in doc_token:
    nodo_filtrado= []
    text_clean = '';
    for word in i:
        if word not in stop_words and re.match('\w',word) and len(word)>3:
            nodo_filtrado.append(word)
            bolsa_clean= bolsa_clean+word+' '
            
    for a in nodo_filtrado:
        text_clean= text_clean+a+' '
            
    doc_tokens_clean.append(nodo_filtrado)
    doc_clean.append(text_clean)

tokens_clean=  nltk.tokenize.word_tokenize(bolsa_clean)


# %% Bolsa de Palabras
import re
import string
bolsa = '';
for a in descripcion:
    if len(a)>2 :
        bolsa = bolsa +a.lower()+' '
# %% Token Bolsa
tokens = nltk.tokenize.word_tokenize(bolsa)

# %% Frecuencias
from nltk.probability import FreqDist
fdist = FreqDist(tokens)

fdist.plot(30)

# %% Stop words
from nltk.corpus import stopwords

string.punctuation = string.punctuation+'”“'
stop_words = stopwords.words('spanish');
filtered_sentence = [w for w in tokens if not w in stop_words and re.match('\w',w) ] 
fdist = FreqDist(filtered_sentence)
fdist.plot(30)

# %% n-gramas
n=2
bigramas =list(nltk.ngrams(filtered_sentence,n))
fqgrama = FreqDist(bigramas)
fqgrama.plot(30)

# %% Colocaciones
from nltk.collocations import *
bigram_measure = nltk.collocations.BigramAssocMeasures();
cont = 0


finder = BigramCollocationFinder.from_words(tokens_clean)
finder.apply_freq_filter(20)
print(finder.nbest(bigram_measure.pmi,100)) ##Informacion mutua punto a punto
   
  

    




