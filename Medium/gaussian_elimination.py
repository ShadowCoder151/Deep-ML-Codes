import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	OG = A.copy()
	m, n = A.shape
	row, col = 0, 0
	ans = []

	while row < m and col < n:
		# if A[row][col] == 0:
		index = np.argmax(np.abs(A[row:, col])) + row
		if A[index, col] == 0:
			col += 1
			continue

		A[[index, row]] = A[[row, index]]
		b[[index, row]] = b[[row, index]]
		# 	print(f'Highest absolute value at {index}')
		# print(f'At row {row}')
		# print(A)
		
		pivot = A[row][col]

		for k in range(row + 1, m):
			div = A[k][col] / pivot
			A[k] = A[k] - div * A[row]
			b[k] = b[k] - div * b[row]
		
		row += 1
		col += 1

	ans = np.zeros(m)
	ans[m - 1] = b[n - 1] / A[m - 1][n - 1]
	for i in range(m - 2, -1, -1):
		S = b[i]
		for j in range(i + 1, n):
			S -= A[i][j] * ans[j]

		ans[i] = S / A[i][i]
	
	return ans


A = np.array([
    [0, 2, 1, 0, 0, 0, 0],
    [2, 6, 2, 1, 0, 0, 0],
    [1, 2, 7, 2, 1, 0, 0],
    [0, 1, 2, 8, 2, 1, 0],
    [0, 0, 1, 2, 9, 2, 1],
    [0, 0, 0, 1, 2, 10, 2],
    [0, 0, 0, 0, 1, 2, 11]
], dtype=float)
b = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)

print(gaussian_elimination(A, b))