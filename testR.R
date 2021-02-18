library(quanteda)
library(readtext)
library(quanteda.textplots)


dat_csv <- read.csv(file = 'gonzalo_text.csv', header = TRUE,sep=';')

corpus_test = corpus(dat_csv$tweet)

dfm_inaug <- corpus_subset(corpus_test) %>% 
  dfm(remove = stopwords('spanish'), remove_punct = TRUE) %>%
  dfm_trim(min_termfreq = 10, verbose = FALSE)

set.seed(100)
textplot_wordcloud(dfm_inaug)

user_dfm <- dfm_select(dfm_inaug, pattern = "@*")
topuser <- names(topfeatures(user_dfm, 50))
head(topuser)

user_fcm <- fcm(user_dfm)


user_fcm <- fcm_select(user_fcm, pattern = topuser)
textplot_network(user_fcm, min_freq = 0.1, edge_color = "orange", edge_alpha = 0.8, edge_size = 5)

textplot_wordcloud(dfm_inaug, min_count = 10,
                   color = c('red', 'pink', 'green', 'purple', 'orange', 'blue'))
