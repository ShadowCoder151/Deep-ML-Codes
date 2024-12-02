import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
	m, n = X.shape
	if method == 'batch':
		for i in range(n_iterations):
			h = X @ weights
			weights = weights - 2 * learning_rate / m * X.T @ (h - y)
	
	elif method == 'stochastic':
		for i in range(n_iterations):
			for j in range(m):
				h = X[j:j+1] @ weights
				weights = weights - 2 * learning_rate * X[j:j + 1].T @ (h - y[j:j+1])

	elif method == 'mini_batch':
		for i in range(n_iterations):
			for j in range(0, m, batch_size):
				h = X[j:j+batch_size] @ weights
				weights = weights - 2 * learning_rate / batch_size * X[j:j+batch_size].T @ (h - y[j:j+batch_size])

	return weights


X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
y = np.array([2, 3, 4, 5])
weights = np.zeros(X.shape[1])
learning_rate = 0.01
n_iterations = 100

# Test Batch Gradient Descent
output = gradient_descent(X, y, weights, learning_rate, n_iterations, method='stochastic')
print(output)