import numpy as np 

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
	U, V = np.eye(2), np.eye(2)

	B = A.T @ A

	theta = 0.5 * np.arctan(B[0, 1] / (B[0, 0] - B[1, 1]))
	G = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

	A = A @ G
	V = V @ G

	U[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0])
	U[:, 1] = A[:, 1] / np.linalg.norm(A[:, 1])

	sigma = np.linalg.norm(A, axis=0)
	# sigma = np.diag(sigma_values)

	return U, sigma, V.T


print(svd_2x2_singular_values(np.array([[1, 2], [3, 4]])))