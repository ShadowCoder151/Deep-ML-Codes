import numpy as np 

def standardize(data):
	return (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    
	
def pca(data: np.ndarray, k: int) -> list[list[int|float]]:
	st_data = standardize(data)
	cov_matrix = np.cov(st_data, rowvar=False)
	values, vectors = np.linalg.eig(cov_matrix)
	
	sorted_indices = np.argsort(values)[::-1]
	vectors = vectors[:, sorted_indices]
	
	principal_components = vectors[:, :k]
	return np.round(principal_components, 4).tolist()


data = np.array([[1, 2], [3, 4], [5, 6]])
k = 1

print(pca(data, k=2))