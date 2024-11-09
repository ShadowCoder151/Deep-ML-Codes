import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	n = len(y)
	
	_, H = np.unique(y, return_counts=True)
	S = 1
	
	for count in H:
		S -= (count / n) ** 2
	
	return round(S, 3)
