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

#%% # CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Fit the CountVectorizer to the training data
vect = CountVectorizer().fit(X_train)

#%% Vectorizacion de bolsa de palabras
X_train_vectorized = vect.transform(X_train)

#%% Entrenar modelo
from sklearn.linear_model import LogisticRegression

# Train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)


#%% Prediccion
from sklearn.metrics import roc_auc_score

# Predict the transformed test documents
predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))

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
#%% Coeficientes
# get the feature names as numpy array
feature_names = np.array(vect.get_feature_names())

# Sort the coefficients from the model
sorted_coef_index = model.coef_[0].argsort()

# Find the 10 smallest and 10 largest coefficients
# The 10 largest coefficients are being indexed using [:-11:-1] 
# so the list returned is in order of largest to smallest
print('Smallest Coefs:\n{}\n'.format(feature_names[sorted_coef_index[:10]]))
print('Largest Coefs: \n{}'.format(feature_names[sorted_coef_index[:-11:-1]]))