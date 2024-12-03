import numpy as np

def rref(matrix):
	matrix = matrix.astype(np.float32)
	m, n = matrix.shape

	for row in range(m):
		if matrix[row, row] == 0:
			nonzero_rel_id = np.nonzero(matrix[row:, row])[0]
			if len(nonzero_rel_id) == 0:
				continue

			matrix[row] += matrix[nonzero_rel_id[0] + row]

		matrix[row] /= matrix[row, row]
		for k in range(m):
			if row != k:
				matrix[k] -= matrix[k, row] * matrix[row]

	return matrix

matrix = np.array([
        [1, 2, -1],
        [2, 4, -1],
        [-2, -4, -3]])

output = rref(matrix)
print(output)

