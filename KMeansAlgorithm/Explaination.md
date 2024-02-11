## K-Means Clustering Algorithm

The K-Means algorithm is a type of unsupervised learning algorithm that is used to classify data into `K` different clusters. The 'K' in K-Means denotes the number of clusters. The algorithm works iteratively to assign each data point to one of `K` groups based on the features that are provided. Data points are clustered based on feature similarity.

## Code Explanation

### Importing Necessary Libraries

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
```

Here, we import the necessary libraries. `load_iris` is used to load the Iris dataset, `train_test_split` is used to split the dataset into training and testing sets, and `numpy` is used for numerical operations.

### Loading the Dataset and Splitting it into Training and Testing Sets

```python
# Load iris dataset
iris = load_iris()
X = iris.data
class_names = iris.target_names

# Split dataset into training set and test set
X_train, X_test = train_test_split(X, test_size=0.3, random_state=1)
```

The Iris dataset is loaded and split into features (`X`) and the corresponding class names (`class_names`). The dataset is then split into training and testing sets, with 70% of the data used for training and 30% used for testing.

### Defining the K-Means Classifier

```python
class KMeans:
    def __init__(self, K=3, max_iters=100):
        self.K = K
        self.max_iters = max_iters

        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]
        # mean feature vector for each cluster
        self.centroids = []
```

The `__init__` method initializes the K-Means classifier with the number of clusters `K` and the maximum number of iterations `max_iters`. It also initializes `clusters`, a list of sample indices for each cluster, and `centroids`, the mean feature vector for each cluster.

```python
    def fit(self, X):
        self.X = X
        self.n_samples, self.n_features = X.shape

        # initialize centroids as random samples
        random_sample_idxs = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idxs]

        # optimization
        for _ in range(self.max_iters):
            # update clusters
            self.clusters = self._create_clusters(self.centroids)
            # update centroids
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            # check for convergence
            if self._is_converged(centroids_old, self.centroids):
                break
```

The `fit` method is used to train the K-Means classifier. It initializes the centroids as random samples from the data. Then, it enters a loop that continues for `max_iters` iterations. In each iteration, it updates the clusters and the centroids, and checks for convergence. If the centroids have not changed from the previous iteration, it breaks out of the loop.

```python
    def predict(self, X):
        labels = np.empty(self.n_samples)

        # assign label to each sample
        for idx, sample in enumerate(X):
            for cluster_idx, cluster in enumerate(self.clusters):
                if idx in cluster:
                    labels[idx] = cluster_idx
        return labels
```

The `predict` method is used to predict the cluster labels for the data points. It assigns each data point to the cluster whose centroid is closest to the point.

```python
    def _get_centroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids
```

The `_get_centroids` method is used to calculate the new centroids, which are the mean of all data points in a cluster.

```python
    def _create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)
        return clusters
```

The `_create_clusters` method is used to create the clusters. Each data point is assigned to the cluster of the closest centroid.

```python
    def _closest_centroid(self, sample, centroids):
        distances = np.zeros(self.K)
        for idx, centroid in enumerate(centroids):
            distances[idx] = np.linalg.norm(sample - centroid)
        closest_index = np.argmin(distances)
        return closest_index
```

The `_closest_centroid` method is used to find the closest centroid to a data point. It calculates the Euclidean distance from the point to each centroid, and returns the index of the closest centroid.

```python
    def _is_converged(self, centroids_old, centroids):
        distances = np.zeros(self.K)
        for idx in range(self.K):
            distances[idx] = np.linalg.norm(centroids_old[idx] - centroids[idx])
        return sum(distances) == 0
```

The `_is_converged` method checks if the algorithm has converged, which is when the centroids do not change from one iteration to the next. It calculates the Euclidean distance between the old and new positions of each centroid, and if the sum of these distances is zero, it means the centroids have not moved and the algorithm has converged.

### Training the Classifier and Making Predictions

```python
# Create a KMeans object
k = KMeans(K=3, max_iters=100)
k.fit(X_train)

# Predict the clusters for the data
y_pred = k.predict(X_train)

# Convert y_pred to int
y_pred = y_pred.astype(int)

print("Predictions:", class_names[y_pred])
```

Finally, we create an instance of the K-Means classifier, train it on the training data, and make predictions on the training data. The predicted cluster labels are then converted to integers and printed.

Please note that K-Means is an unsupervised learning algorithm and doesn't use target data `y` for training. The true labels `y_test` are only used here for evaluating the clustering performance, which is not typically done for unsupervised learning. In a real-world scenario, you might not have `y_test` available.
