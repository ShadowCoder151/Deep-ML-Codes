def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	det = (a * d - b * c)
	
	a, b, c, d = a / det, b / det, c / det, d / det
	return [[d, -b], [-c, a]]