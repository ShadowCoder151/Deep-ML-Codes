import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))
	D = np.zeros_like(A)
	np.fill_diagonal(D, np.diag(A))
	
	R = A - D
	for _ in range(n):
		x = np.linalg.inv(D) @ (b - R @ x)
	return np.round(x, 4)