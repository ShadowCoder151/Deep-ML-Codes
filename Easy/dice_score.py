import numpy as np

def dice_score(y_true, y_pred):
	# count = np.sum((y_true == 1) & (y_pred == 1))
	count = np.logical_and(y_true, y_pred).sum()
	total = np.sum(y_true) + np.sum(y_pred)
	
	if np.sum(y_true) == 0 or np.sum(y_pred) == 0:
		return 0.0
	res = count * 2 / total 
	return round(res, 3)
