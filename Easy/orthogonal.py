def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	def dot(a, b):
		return sum(a[i] * b[i] for i in range(len(a)))
	
	S = dot(v, L) / dot(L, L)
	
	res = []
	for i in range(len(v)):
		res.append(round(S * L[i], 3))
		
	return res
