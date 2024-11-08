import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	T = np.exp(scores)
	S = np.sum(T)
	scores = scores - np.log(S)
	return scores