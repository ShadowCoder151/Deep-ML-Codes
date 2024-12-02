import numpy as np

def calculate_correlation_matrix(X, Y=None):
	X = X.astype('float64')
	mean_x = np.mean(X, axis=0)
	std_x = np.std(X, axis=0)
	for i in range(X.shape[0]):
		X[i] = (X[i] - mean_x) / std_x
	if Y is not None:
		Y = Y.astype('float64')
		mean_y = np.mean(Y, axis=0)
		std_y = np.std(Y, axis=0)
		for i in range(Y.shape[0]):
			Y[i] = (Y[i] - mean_y) / std_y
		return X.T @ Y / X.shape[0]
	
	else:
		return X.T @ X / X.shape[0]


X = np.array([[1, 2],
            [3, 4],
            [5, 6]])
output = calculate_correlation_matrix(X)
print(output)
# Output:
# [[1. 1.]
#  [1. 1.]]
    