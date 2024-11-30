import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	ans = x_ini if x_ini is not None else np.zeros_like(b)
	rows, cols = A.shape

	for _ in range(n):
		for i in range(rows):
			S = b[i]
			for j in range(cols):
				if i != j:
					S -= ans[j] * A[i][j]
			ans[i] = S / A[i][i]
	
	return ans
			

A = np.array([[4, 1, 2], [3, 5, 1], [1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)

n = 100
print(gauss_seidel(A, b, n))