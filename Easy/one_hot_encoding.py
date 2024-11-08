import numpy as np

def to_categorical(x, n_col=None):
	if n_col is None:
		n_col = np.max(x) + 1

	res = np.zeros((x.shape[0], n_col))
	res[np.arange(x.shape[0]), x] = 1
	return res