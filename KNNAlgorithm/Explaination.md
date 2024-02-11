## k-Nearest Neighbors (k-NN) Algorithm

The k-NN algorithm is a type of instance-based learning algorithm. It classifies instances based on their similarity to instances in the training dataset. The 'k' in k-NN refers to the number of nearest neighbors the algorithm considers when making a prediction.

## Code Explanation

### Importing Necessary Libraries

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter
```

Here, we import the necessary libraries. `load_iris` is used to load the Iris dataset, `train_test_split` is used to split the dataset into training and testing sets, `numpy` is used for numerical operations, and `Counter` is used to count the number of occurrences of each class in the k nearest neighbors.

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

### Defining the k-NN Classifier

```python
class KNN:
    def __init__(self, k=3):
        self.k = k
```

The `__init__` method initializes the k-NN classifier with the number of neighbors `k`.

```python
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
```

The `fit` method is used to train the k-NN classifier. It simply stores the training data.

```python
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
```

The `predict` method is used to predict the classes of a set of instances. It applies the `_predict` method to each instance in `X`.

```python
    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
```

The `_predict` method is used to predict the class of a single instance. It computes the Euclidean distance between the input instance and all instances in the training data, selects the `k` nearest instances, and returns the most common label among them.

### Training the Classifier and Making Predictions

```python
# Create a k-NN classifier with 3 neighbors
knn = KNN(k=3)

# Train the model using the training sets
knn.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = knn.predict(X_test)

# Print class names instead of class numbers
print("Predictions:", class_names[y_pred])
```

Finally, we create an instance of the k-NN classifier, train it on the training data, and make predictions on the test data. The predicted class numbers are then mapped to their corresponding names using `class_names` before being printed.
