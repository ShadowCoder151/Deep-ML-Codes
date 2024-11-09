import numpy as np

def compressed_row_sparse_matrix(matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values, column_indices, row_pointer = [], [], [0]
	m, n = len(matrix), len(matrix[0])
	
	for i in range(m):
		count = 0
		for j in range(n):
			if matrix[i][j] != 0:
				values.append(matrix[i][j])
				column_indices.append(j)
				count += 1
		row_pointer.append(row_pointer[-1] + count)
	return values, column_indices, row_pointer
