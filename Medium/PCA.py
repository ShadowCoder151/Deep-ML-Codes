import numpy as np 

def standardize(data):
	m, n = data.shape
	
	for i in range(n):
		y = data[:, i]
		M = np.mean(y)
		S = np.std(y)
		data[:, i] = (y - M) / S

	return data
    
	
def pca(data: np.ndarray, k: int) -> list[list[int|float]]:
	# Your code here
	st_data = standardize(data)
	cov_matrix = np.cov(st_data, rowvar=False)

	values, vectors = np.linalg.eig(cov_matrix)
	vectors = np.round(vectors, 4)

	S = list(zip(values, vectors))
	S.sort(reverse=True, key=lambda x: x[0])

	return [x[1] for x in S[:k]]


data = np.array([[1, 2], [3, 4], [5, 6]])
k = 1

print(pca(data, k=2))