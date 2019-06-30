from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


clf = KNeighborsClassifier(n_neighbors=2)
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)


# General
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf.fit(X_train_tfidf, twenty_train.target)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predicted)
print("Accuracy score of general tdfidf vector ")
print(score)


# Bigram
tfidf_Vect1 = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf1 = tfidf_Vect1.fit_transform(twenty_train.data)
clf.fit(X_train_tfidf1, twenty_train.target)
X_test_tfidf1 = tfidf_Vect1.transform(twenty_test.data)
predicted1 = clf.predict(X_test_tfidf1)
score = metrics.accuracy_score(twenty_test.target, predicted1)
print("Accuracy score bigram condition tdfidf vector ")
print(score)

# stopwords
tfidf_Vect2 = TfidfVectorizer(stop_words='english')
X_train_tfidf2 = tfidf_Vect2.fit_transform(twenty_train.data)
clf.fit(X_train_tfidf2, twenty_train.target)
X_test_tfidf2 = tfidf_Vect2.transform(twenty_test.data)
predicted2 = clf.predict(X_test_tfidf2)
score = metrics.accuracy_score(twenty_test.target, predicted2)
print("Accuracy score with stopwords condition tdfidf vector ")
print(score)
