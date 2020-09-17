# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:43:17 2020

@author: Juan Castillo
"""
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