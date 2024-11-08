import numpy as np

def make_diagonal(x):
	return np.identity(x.shape[0]) * x