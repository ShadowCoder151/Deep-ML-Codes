import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
	B = A.T @ A
	e1, v1 = np.linalg.eig(B)
	
	C = A @ A.T
	e2, v2 = np.linalg.eig(C)
	

U,s,V = svd_2x2(np.array([[1, 2], [3, 4]]))
result = U @ np.diag(s) @ V
print(result)