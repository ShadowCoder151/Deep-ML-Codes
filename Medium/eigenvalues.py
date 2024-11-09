import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	
	B, C = a + d, a * d - b * c
	
	dis = math.sqrt(B ** 2 - 4 * C)
	return (B + dis) / 2, (B - dis) / 2