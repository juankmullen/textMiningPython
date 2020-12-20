#%% carga de datos
import pandas as pd
import numpy as np

# Read in the data
df = pd.read_csv('data/Amazon_Unlocked_Mobile.csv')

# Sample the data to speed up computation
# Comment out this line to match with lecture
df = df.sample(frac=0.1, random_state=10)


#%%Limpieza de datos y creacion de etiqueta
df.dropna(inplace=True)

# Se borra el valor medio [1,5]
df = df[df['Rating'] != 3]

#Se crea nueva variable etiqueta
df['Positively Rated'] = np.where(df['Rating'] > 3, 1, 0)

#%% Particion de datos
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['Reviews'], 
                                                    df['Positively Rated'], 
                                                    random_state=0)
#%% TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer

# Fit the TfidfVectorizer to the training data specifiying a minimum document frequency of 5
vect = TfidfVectorizer(min_df=5).fit(X_train)

#%% Prediccion
from sklearn.linear_model import LogisticRegression
X_train_vectorized = vect.transform(X_train)

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))

#%% Matriz de confusion
from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, predictions)
import seaborn as sns
sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')
#%% F1 Score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
f1_score_metric = f1_score(y_test, predictions)
precision = accuracy_score(y_test, predictions)

#%% Clasificacion report
from sklearn.metrics import classification_report
target_names = ['class 0', 'class 1',]
report = classification_report(y_test, predictions, target_names=target_names)
#%% Mediciones
from sklearn.metrics import roc_auc_score

feature_names = np.array(vect.get_feature_names())

sorted_coef_index = model.coef_[0].argsort()

print('Smallest tfidf:\n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest tfidf: \n{}'.format(feature_names[sorted_coef_index[:-11:-1]]))
print('AUC: ', roc_auc_score(y_test, predictions))