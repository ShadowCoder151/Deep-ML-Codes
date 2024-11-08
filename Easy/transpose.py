def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	m, n = len(a), len(a[0])
	
	b = [[0] * m for _ in range(n)]
	
	for j in range(m):
		for i in range(n):
			b[i][j] = a[j][i]
	return b