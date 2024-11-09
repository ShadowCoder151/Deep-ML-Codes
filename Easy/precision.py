import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	
	return tp / (tp + fp)
	