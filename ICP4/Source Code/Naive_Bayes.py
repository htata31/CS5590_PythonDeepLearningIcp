# Data Preprocessing

# Importing the libraries
import pandas as pd
import matplotlib as plt
import numpy as np

# Importing the dataset
dataset = pd.read_csv('glass.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
acc_naive = accuracy_score(y_test, y_pred )

print("The Accuracy score is",round(acc_naive * 100,2))

