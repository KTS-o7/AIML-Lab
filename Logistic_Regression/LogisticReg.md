## Code Explained

```python
# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
```
This block of code imports the necessary libraries for the script. These libraries provide functions for loading datasets, splitting data into training and test sets, preprocessing data, creating a logistic regression model, calculating accuracy, and plotting data.

```python
# Load Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features (sepal length and width)
y = iris.target
```
Here, the Iris dataset is loaded. The Iris dataset is a popular dataset in machine learning and it contains measurements of 150 iris flowers from three different species. `X` is assigned the first two features of the dataset (sepal length and width), and `y` is assigned the target variable (species of iris).

```python
# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
The dataset is split into a training set and a test set. 80% of the data is used for training the model and the remaining 20% is used for testing the model.

```python
# Standardize features
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)
```
The features are standardized by removing the mean and scaling to unit variance. This is done to make the algorithm less sensitive to the scale of features.

```python
# Create a Logistic Regression classifier
classifier = LogisticRegression(random_state=42)
```
A Logistic Regression classifier is created. Logistic Regression is a machine learning algorithm used for binary classification problems.

```python
# Train the classifier
classifier.fit(X_train_std, y_train)
```
The classifier is trained using the training data.

```python
# Predict the test set results
y_pred = classifier.predict(X_test_std)
```
The trained classifier is used to predict the species of iris for the test data.

```python
# Print the accuracy
print('Accuracy: %.4f' % accuracy_score(y_test, y_pred))
```
The accuracy of the classifier is calculated by comparing the predicted species of iris to the actual species of iris in the test data.

```python
# Plot the decision boundary
x_min, x_max = X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1
y_min, y_max = X_train_std[:, 1].min() - 1, X_train_std[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X_train_std[:, 0], X_train_std[:, 1], c=y_train, alpha=0.8)
plt.title('Logistic Regression Decision Boundaries')
plt.xlabel('Sepal length')
plt.xlabel('Sepal width')

plt.savefig('plot.png')
```
This block of code plots the decision boundaries of the Logistic Regression classifier. The decision boundaries separate the different species of iris. The plot is saved as 'plot.png'.

