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

# Fitting SVC with linear kernal to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Accuracy Scores
from sklearn.metrics import accuracy_score
acc_svc = accuracy_score(y_test, y_pred )

print("The Accuracy score of SVC with linear kernal is",round(acc_svc * 100,2))




# Fitting SVC with rbf kernal to the Training set
classifier = SVC(kernel='rbf')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred_rbf = classifier.predict(X_test)

# Accuracy Scores
acc_svc_rbf = accuracy_score(y_test, y_pred_rbf )

print("The Accuracy score of SVC with linear kernal is",round(acc_svc_rbf * 100,2))


