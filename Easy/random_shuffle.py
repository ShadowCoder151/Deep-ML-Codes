import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	np.random.seed(seed)
	np.random.shuffle(X)
	
	np.random.seed(seed)
	np.random.shuffle(y)
	return X, y