import pandas as pd
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dataset = pd.read_csv('../resources/imdb_reviews.csv', encoding = "ISO-8859-1")
dataset.count()

reviews = dataset['review'].values
classes = dataset['label'].values

vectorizer = CountVectorizer(analyzer="word")
freq_reviews = vectorizer.fit_transform(reviews)

modelo = MultinomialNB()
modelo.fit(freq_reviews, classes)

def predict(msg):
    freq_testes = vectorizer.transform([msg])
    return str(modelo.predict(freq_testes)[0])
