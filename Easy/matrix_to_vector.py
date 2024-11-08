def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	m, n = len(a), len(a[0])
	
	if len(b) != n:
		return -1
	
	res = [0 for _ in range(len(b))]
	for i in range(m):
		S = 0
		for j in range(len(b)):
			S += a[i][j] * b[j]
		res[i] = S
	
	return res
	
	