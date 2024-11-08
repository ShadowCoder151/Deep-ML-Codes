def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	m, n = len(matrix), len(matrix[0])
	
	if mode == 'row':
		for i in range(m):
			S = 0
			for j in range(n):
				S += matrix[i][j]
			means.append(S / n)
	else:
		for j in range(n):
			S = 0
			for i in range(m):
				S += matrix[i][j]
			means.append(S / m)
	
	return means