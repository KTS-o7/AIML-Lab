# Code Explained :

1. **Importing necessary libraries:**

   ```python
   import numpy as np
   from sklearn import datasets
   from sklearn.model_selection import train_test_split
   from sklearn.preprocessing import StandardScaler
   import matplotlib.pyplot as plt
   ```

   This block of code imports the necessary libraries. `numpy` is used for numerical operations, `sklearn.datasets` is used to load the Iris dataset, `sklearn.model_selection.train_test_split` is used to split the dataset into training and testing sets, `sklearn.preprocessing.StandardScaler` is used for feature scaling, and `matplotlib.pyplot` is used for plotting.

2. **Defining the sigmoid function:**

   ```python
   def sigmoid(z):
       return 1.0 / (1.0 + np.exp(-z))
   ```

   The sigmoid function is used as the activation function in logistic regression. It maps any real-valued number to the (0, 1) range, which can be treated as a probability.

3. **Defining the cost function:**

   ```python
   def cost_function(h, y):
       return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
   ```

   The cost function is used to measure the performance of the model. It calculates the error between the model's predictions and the actual values. The goal is to minimize this cost function.

4. **Defining the gradient computation:**

   ```python
   def gradient(X, h, y):
       return np.dot(X.T, (h - y)) / y.shape[0]
   ```

   The gradient of the cost function is used in the gradient descent algorithm to update the weights. It points in the direction of the greatest rate of increase of the cost function.

5. **Defining the logistic regression function:**

   ```python
   def logistic_regression(X, y, num_iterations, learning_rate):
       weights = np.zeros(X.shape[1])
       for i in range(num_iterations):
           z = np.dot(X, weights)
           h = sigmoid(z)
           gradient_val = gradient(X, h, y)
           weights -= learning_rate * gradient_val
       return weights
   ```

   This function performs logistic regression using gradient descent. It initializes the weights to zero and then iteratively updates them by moving in the direction of steepest descent of the cost function. The learning rate controls the size of the updates.

6. **Loading the dataset and preprocessing:**

   ```python
   iris = datasets.load_iris()
   X = iris.data[:, :2]
   y = (iris.target != 0) * 1
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   sc = StandardScaler()
   X_train_std = sc.fit_transform(X_train)
   X_test_std = sc.transform(X_test)
   ```

   This block of code loads the Iris dataset, selects the first two features and converts the problem into a binary classification problem. It then splits the dataset into a training set and a test set, and standardizes the features using `StandardScaler`.

7. **Performing logistic regression:**

   ```python
   weights = logistic_regression(X_train_std, y_train, num_iterations=5000, learning_rate=0.1)
   ```

   This line performs logistic regression on the training data. The weights returned by the function are used to make predictions.

8. **Making predictions:**

   ```python
   y_pred = sigmoid(np.dot(X_test_std, weights)) > 0.5
   ```

   This line makes predictions on the test data. The sigmoid function is applied to the linear combination of the test data and the weights, and the result is thresholded at 0.5 to make binary predictions.

9. **Printing the accuracy:**

   ```python
   print('Accuracy: %.4f' % np.mean(y_pred == y_test))
   ```

   This line prints the accuracy of the model on the test data.

10. **Plotting the decision boundary:**
    ```python
    x_min, x_max = X_train_std[:, 0].min() - 1, X_train_std[:, 0].max() + 1
    y_min, y_max = X_train_std[:, 1].min() - 1, X_train_std[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = sigmoid(np.dot(np.c_[xx.ravel(), yy.ravel()], weights)) > 0.5
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X_train_std[:, 0], X_train_std[:, 1], c=y_train, alpha=0.8)
    plt.title('Logistic Regression Decision Boundaries')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.savefig('plot.png')
    ```
    This block of code plots the decision boundary of the logistic regression model. It creates a grid of points, makes predictions at each point, and then plots the decision boundary as a contour plot. The training data is also plotted as a scatter plot.
