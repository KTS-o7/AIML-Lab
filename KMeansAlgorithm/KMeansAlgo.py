import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# Load iris dataset
iris = load_iris()
X = iris.data
class_names = iris.target_names

# Split dataset into training set and test set
X_train, X_test = train_test_split(X, test_size=0.3, random_state=1)

class KMeans:
    def __init__(self, K=3, max_iters=100):
        self.K = K
        self.max_iters = max_iters

        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]
        # mean feature vector for each cluster
        self.centroids = []

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

    def predict(self, X):
        labels = np.empty(self.n_samples)

        # assign label to each sample
        for idx, sample in enumerate(X):
            for cluster_idx, cluster in enumerate(self.clusters):
                if idx in cluster:
                    labels[idx] = cluster_idx
        return labels

    def _get_centroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids

    def _create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)
        return clusters

    def _closest_centroid(self, sample, centroids):
        distances = np.zeros(self.K)
        for idx, centroid in enumerate(centroids):
            distances[idx] = np.linalg.norm(sample - centroid)
        closest_index = np.argmin(distances)
        return closest_index

    def _is_converged(self, centroids_old, centroids):
        distances = np.zeros(self.K)
        for idx in range(self.K):
            distances[idx] = np.linalg.norm(centroids_old[idx] - centroids[idx])
        return sum(distances) == 0

    

# Create a KMeans object
k = KMeans(K=3, max_iters=100)
k.fit(X_train)

# Predict the clusters for the data
y_pred = k.predict(X_train)

# Convert y_pred to int
y_pred = y_pred.astype(int)

print("Predictions:", class_names[y_pred])





