import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	y_pred = X @ w
	sq_loss = np.sum((y_true - y_pred) ** 2) / X.shape[0]
	
	wt_loss = np.sum(w ** 2)
	return sq_loss + alpha * wt_loss
	
