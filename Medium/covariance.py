def matrixmul(a, b):
	
	m, n = len(a), len(a[0])
	p, q = len(b), len(b[0])
	
	res = [[0] * q for _ in range(m)]
	
	for k in range(n):
		for i in range(m):
			for j in range(q):
				res[i][j] += a[i][k] * b[k][j]
	return res


def transpose(a):
	m, n = len(a), len(a[0])
	
	b = [[0] * m for _ in range(n)]
	
	for j in range(m):
		for i in range(n):
			b[i][j] = a[j][i]
	return b

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	m, n = len(vectors), len(vectors[0])
	
	for i in range(m):
		mean = sum(vectors[i]) / n
		vectors[i] = [(num - mean) for num in vectors[i]]

	vectors_t = transpose(vectors)
	covariance_matrix = matrixmul(vectors, vectors_t)

	for i in range(len(covariance_matrix)):
		for j in range(len(covariance_matrix[0])):
			covariance_matrix[i][j] /= (n - 1)

	return covariance_matrix

	
	