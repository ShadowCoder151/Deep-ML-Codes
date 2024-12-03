import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	# calculate initial residual vector
	
	xk = np.zeros_like(b) if x0 is None else x0
	rk = b - A @ xk
	pk = rk

	for _ in range(n):
		if np.linalg.norm(rk) < tol:
			break
		alpha_k = np.dot(rk, rk) / (pk.T @ A @ pk)

		xk_1 = xk + alpha_k * pk
		rk_1 = rk - alpha_k * (A @ pk)

		beta_k = np.dot(rk_1, rk_1) / np.dot(rk, rk)

		pk_1 = rk_1 + beta_k * pk

		xk, rk, pk = xk_1, rk_1, pk_1

	return xk


A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
n = 5

print(conjugate_gradient(A, b, n))