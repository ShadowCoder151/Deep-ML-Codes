import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	average = np.mean(y_true)
	TSS = np.sum((y_true - average) ** 2)
	RSS = np.sum((y_true - y_pred) ** 2)
	return 1 - RSS / TSS
