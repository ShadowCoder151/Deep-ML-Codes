import numpy as np

def jaccard_index(y_true, y_pred):
	count = sum(y_true[i] == y_pred[i] == 1 for i in range(len(y_true)))
	
	result = count / (np.sum(y_true == 1) + np.sum(y_pred == 1) - count)
	return round(result, 3)
