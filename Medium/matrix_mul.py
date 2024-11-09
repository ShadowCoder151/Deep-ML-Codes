def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	m, n = len(a), len(a[0])
	p, q = len(b), len(b[0])
	
	if n != p:
		return -1
	
	res = [[0] * q for _ in range(m)]
	
	for k in range(n):
		for i in range(m):
			for j in range(q):
				res[i][j] += a[i][k] * b[k][j]
	return res