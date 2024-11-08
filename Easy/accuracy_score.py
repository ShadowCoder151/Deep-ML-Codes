import numpy as np

def accuracy_score(y_true, y_pred):
	tp = np.sum((y_true == 1) & (y_pred == 1))
	tn = np.sum((y_true == 0) & (y_pred == 0))
	
	return (tp + tn) / y_true.shape[0]