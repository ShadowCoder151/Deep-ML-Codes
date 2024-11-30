import numpy as np

def rref(matrix):
	matrix = matrix.astype(float)
	m, n = matrix.shape
	row, col = 0, 0
	ans = []

	while row < m and col < n:
		# if A[row][col] == 0:
		index = np.argmax(np.abs(matrix[row:, col])) + row
		if matrix[index, col] == 0:
			col += 1
			continue

		matrix[[index, row]] = matrix[[row, index]]
		# 	print(f'Highest absolute value at {index}')
		# print(f'At row {row}')
		# print(A)
		
		pivot = matrix[row][col]
		matrix[row] = matrix[row] / pivot

		for k in range(m):
			if k != row:
				matrix[k] = matrix[k] -  matrix[k, col] * matrix[row]
		
		row += 1
		col += 1
		
	'''non_zero = matrix[np.any(matrix != 0, axis=1)]
	zero = matrix[~np.any(matrix != 0, axis=1)]
	return np.vstack((non_zero, zero))'''
	return matrix

matrix = np.array([
        [1, 2, -1],
        [2, 4, -1],
        [-2, -4, -3]])

output = rref(matrix)
print(output)

