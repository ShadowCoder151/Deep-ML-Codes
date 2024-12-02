import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
	m, n = X.shape

	ans = [np.ones(m)]

	for d in range(1, degree + 1):
		for comb in combinations_with_replacement(range(n), d):
			ans.append(np.prod(X[:, comb], axis=1))
	
	return np.vstack(ans).T

X = np.array([[2, 3],
                  [3, 4],
                  [5, 6]])
degree = 2
output = polynomial_features(X, degree)
print(output)