import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	y =  y.reshape(m, 1)
	for i in range(iterations):
		h = X @ theta
		theta = theta - alpha / m * X.T @ (h - y)
	
	return theta