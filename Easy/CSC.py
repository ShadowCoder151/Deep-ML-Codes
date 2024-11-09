def compressed_col_sparse_matrix(matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	vals, row_idx, col_ptr = [], [], [0] 
	m, n = len(matrix), len(matrix[0])
	
	for j in range(n):
		count = 0
		for i in range(m):
			if matrix[i][j] != 0:
				vals.append(matrix[i][j])
				row_idx.append(j)
				count += 1
		col_ptr.append(col_ptr[-1] + count)
	return vals, row_idx, col_ptr 
