
## Naive Bayes Classifier

The Naive Bayes classifier is a simple and effective classification algorithm that uses probabilities and Bayes' theorem to predict the class of an instance. The 'naive' part comes from the assumption that all features are independent of each other, which is not always the case in real-world data, but it simplifies the calculations and often works well in practice.

## Code Explanation

### Importing Necessary Libraries

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
```

Here, we import the necessary libraries. `numpy` is used for numerical operations, `load_iris` is used to load the Iris dataset, and `train_test_split` is used to split the dataset into training and testing sets.

### Loading the Dataset and Splitting it into Training and Testing Sets

```python
# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
```

The Iris dataset is loaded and split into features (`X`) and target (`y`). The target names are stored in `class_names`. The dataset is then split into training and testing sets, with 70% of the data used for training and 30% used for testing.

### Defining the Naive Bayes Classifier

```python
class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # calculate mean, var, and prior for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors =  np.zeros(n_classes, dtype=np.float64)

        for idx, c in enumerate(self._classes):
            X_c = X[y==c]
            self._mean[idx, :] = X_c.mean(axis=0)
            self._var[idx, :] = X_c.var(axis=0)
            self._priors[idx] = X_c.shape[0] / float(n_samples)
```

The `fit` method is used to train the Naive Bayes classifier. It calculates the mean, variance, and prior probabilities for each class. These are stored in `_mean`, `_var`, and `_priors` respectively. The mean and variance are used to calculate the likelihood of a feature given a class (using the Gaussian probability density function), and the priors are used to calculate the prior probabilities of each class.

```python
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
```

The `predict` method is used to predict the classes of a set of instances. It applies the `_predict` method to each instance in `X`.

```python
    def _predict(self, x):
        posteriors = []

        # calculate posterior probability for each class
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            class_conditional = np.sum(np.log(self._pdf(idx, x)))
            posterior = prior + class_conditional
            posteriors.append(posterior)
            
        # return class with highest posterior probability
        return self._classes[np.argmax(posteriors)]
```

The `_predict` method is used to predict the class of a single instance. It calculates the posterior probability for each class and returns the class with the highest posterior probability. The posterior probability is calculated as the sum of the log prior and the log class conditional probability.

```python
    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(- (x-mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator
```

The `_pdf` method is used to calculate the probability density function of the Gaussian distribution. This is used to calculate the likelihood of a feature given a class.

### Training the Classifier and Making Predictions

```python
# Create a Naive Bayes Classifier
nb = NaiveBayes()

# Train the model using the training sets
nb.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = nb.predict(X_test)

# Print class names instead of class numbers
print("Predictions:", class_names[y_pred])
```

Finally, we create an instance of the Naive Bayes classifier, train it on the training data, and make predictions on the test data. The predicted class numbers are then mapped to their corresponding names using `class_names` before being printed.

This is a basic implementation of the Naive Bayes classifier and may not perform as well as optimized libraries like `sklearn`, but it should give you a good understanding of how the algorithm works. It's also worth noting that this implementation assumes that the features follow a Gaussian distribution, which may not be the case for all datasets. Other types of Naive Bayes classifiers (like Multinomial Naive Bayes or Bernoulli Naive Bayes) may be more appropriate for data that follows a different distribution. 

