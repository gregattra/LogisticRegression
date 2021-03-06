# this is a logistic regression classifier that determines if the input data is a certain type of cancer
# it is a single class classifier model

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datacleaner
import scipy
from compute_cost import compute_cost
from gradient_descent import gradient_descent
from sigmoid import sigmoid

# import and clean data
data = pd.read_csv('dataset_single.csv')
clean_data = datacleaner.autoclean(data, True).values
X = np.matrix(clean_data[:, 0:9])
y = np.matrix(clean_data[:, 9:10])

# size of data
m = y.shape[0]

# preprocess y to convert 4 to 1 and 2 to 0 since this is a single classifier model
for i in range(0, m):
    y[i] = 1 if y[i] == 4 else 0

# add ones to X
X0 = np.ones((X.shape[0], 1))
X = np.hstack((X0, X))

# initialize thetas
theta = np.zeros((X.shape[1], 1))

# initialize training params
alpha = 0.01
iterations = 10000

# test cost function
J, grad = compute_cost(X, y, theta)

# run gradient descent
[theta, J_history] = gradient_descent(X, y, theta, alpha, iterations)

# plot J_history to make sure gradient descent worked
plt.plot(range(iterations), J_history)

# check accuracy
z = X.dot(theta)
h = sigmoid(z)
acc = 0
for i in range(0, m):
    acc += 1 if (h[i] >= 0.5 and y[i] == 1) or (h[i] < 0.5 and y[i] == 0) else 0

# print accuracy (~ 96%)
print('Accuracy: ' + str(acc / m))
