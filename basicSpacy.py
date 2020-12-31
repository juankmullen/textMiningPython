# Import spaCy and load the language library
import spacy
import en_core_web_sm
import es_core_news_sm
nlp = es_core_news_sm.load()

#%% Ejemplo de tokenizacion
doc = nlp(u'Aunque comúnmente se le atribuye a John Lennon por su canción "Beautiful Boy", \
la frase "La vida es lo que nos pasa mientras hacemos otros planes" fue escrita por \
dibujante Allen Saunders y publicado en Reader \'s Digest en 1957, cuando Lennon tenía 17 años.')

# Print each token separately
for token in doc:
    print(token.text, token.pos_, token.dep_,token.lemma_,token.is_alpha,token.is_stop)
    

#%% Separar oraciones
doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')
for sentence in doc.sents:
    print(sentence)
    
# Inicio de una oracion ?    
print(doc[7].is_sent_start)

#%% Entidades
doc8 = nlp(u'Apple construirá una nueva fabrica en Hong Kong por 6 millones de dolares')

for token in doc8:
    print(token.text, end='|')

print('\n----')

for ent in doc8.ents:
    print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
   

