import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	res = []
	
	for i in range(0, X.shape[0], batch_size):
		Xi = X[i:i + batch_size]
		if y is not None:
			yi = y[i:i+batch_size]
			res.append([Xi, yi])
		else:
			res.append(Xi)
	return res