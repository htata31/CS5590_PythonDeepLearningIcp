# Data Preprocessing

# Importing the libraries
import pandas as pd
from pathlib import Path

# Importing the dataset
dataset = pd.read_csv(Path('Dataset2/glass.csv'))
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting SVC with linear kernal to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel='rbf')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred_train = classifier.predict(X_train)
y_pred_test = classifier.predict(X_test)

# Accuracy Scores
from sklearn.metrics import accuracy_score
train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print("The train Accuracy score of SVC with linear kernal is", round(train_acc * 100, 2))
print("The test Accuracy score of SVC with linear kernal is", round(test_acc * 100, 2))





