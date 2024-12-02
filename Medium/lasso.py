import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
	n_samples, n_features = X.shape

	weights = np.zeros(n_features)
	bias = 0

	print(weights.shape)
	print(X.shape)

	for _ in range(max_iter):
		y_hat = X @ weights + bias
		w_grad = -1 / len(X) * np.dot(X.T, (y - y_hat)) + alpha * np.sign(weights)
		b_grad = -1 / len(X) * np.sum(y - y_hat)

		weights = weights - learning_rate * w_grad
		bias = bias - learning_rate * b_grad
	
	return weights, bias


X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

alpha = 0.1
weights, bias = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000)
print(weights, bias)