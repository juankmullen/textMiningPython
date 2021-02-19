library(quanteda)
library(readtext)
library(quanteda.textplots)
library(quanteda.textmodels)
library(stringr)
library(topicmodels)
library(tidyverse)
library(tidytext)
library(NLP)
library(tm)
library(wordcloud)
library(cluster)

set.seed(100)
#filecsv = 'penaloza_text.csv'
#filecsv = 'kast_text.csv'
#filecsv = 'daniel_text.csv'
#filecsv = 'lavin_text.csv'
filecsv = 'gonzalo_text.csv'

name = 'Gonzalo de la Carrera'
#name = 'Daniela Peñaloza'
#name = 'Daniel Jadue'
#name  = 'Kast'
#name  = 'Lavin'

#setear carpeta con archivos
setwd("C:/Repositorios/Otros/textMiningPython")

# stpwords español
stop <- stopwords('spanish')

## basura ajena a las stopwors
eliminar <-c('gonzalo','c','rt','xd','da','si','cmo','q','t','3',
                      'p','s','si','d','m','ser','mas','carrera','así','asi',
                      'bien','sr','x','de','la','a','el','condes','ja','las','hoy')

stop <- c(stop,eliminar)

#Extraccion de data
dat_csv <- read.csv(file = filecsv , header = TRUE,sep=';', encoding = "UTF-8")


#minusculas
clean <-  data.frame("text"=tolower(dat_csv$tweet))

# stopword
clean$text <- removeWords(clean$text, words = stop)

#eliminacion de url
clean <- data.frame("text"=gsub(" ?(f|ht)tp(s?)://(.*)[.][a-z]+", "", clean$text))

#Eliminar usuarios
clean$text <-gsub("@([A-Za-z0-9_]{1,15})", "", clean$text)

#Eliminar hasgtag
clean$text <-gsub("#([A-Za-z0-9_]{1,15})", "", clean$text)

#Eliminar ../XXX
clean$text  <- gsub('(...)?/(.*)', "", clean$text)

#Solo alfanumericos
clean$text  <- gsub('[^A-Za-zÀ-ÿ ]', "", clean$text)

#mas de un espacio
clean$text  <- gsub('\\s{2}(\\s*)?', " ", clean$text)

# espacios inicio y fin
clean$text <- str_trim(clean$text)

# espacios en blanco excesivos
clean$text <- stripWhitespace(clean$text)


#Limpieza valores vacios y NA
clean <- clean[clean$text != '', ]
clean <- clean[!is.na(clean$text),]

#Asignacion nuevos valores 
clean <-data.frame('text'=clean)

n_grams = 2
repeticiones <- clean %>%
                unnest_tokens(bigrama,
                text,
                token = "ngrams",
                n = n_grams)


repeticiones %>%
  filter(!is.na(bigrama)) %>%
  count(bigrama, sort = T) %>%
  top_n(10) %>%
  ggplot() +
  geom_col(aes(y = n , x = reorder(bigrama,n)),
           fill = "maroon") +
  coord_flip() +
  theme_linedraw() + 
  labs(x = "Bigramas", y = "Frecuencia") + 
  ggtitle("Trigramas más frecuentes ", subtitle = name)


## Relaciones
corpus <- VCorpus(VectorSource(clean$text))

## mapeo de corpus
nov_ptd <- tm_map(corpus, PlainTextDocument)

#nube de palabras
wordcloud(nov_ptd,min.freq = 3, max.words = 300, random.order = F, colors = brewer.pal(name = "Dark2", n = 8))

#matriz de terminos
nov_tdm <- TermDocumentMatrix(nov_ptd)
nov_mat <- as.matrix(nov_tdm)


##se quitan palabras dispersas,definir  sparse alto significa valores comunes
nov_new <- removeSparseTerms(nov_tdm, sparse = .98)

nov_dist <- dist(nov_new, method = "euclidian")

nov_hclust <-  hclust(nov_dist, method = "complete")

plot(nov_hclust, main = paste("Dendrograma",name,sep=" "), sub = "", xlab = "")

# K es indefinido automaticamente
rect.hclust(nov_hclust, k = 4, border="blue")

#dendograma ordenado
nov_agnes <- agnes(nov_dist, method = "average")
plot(nov_agnes, which.plots = 2, main = paste("Dendrograma",name,sep=" "), sub = "", xlab = "")

