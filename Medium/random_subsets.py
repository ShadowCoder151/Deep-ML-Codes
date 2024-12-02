import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
	m = X.shape[0]
	np.random.seed(seed)
	s_size = m if replacements else m // 2

	indices = []
	for _ in range(n_subsets):
		idx = np.random.choice(m, s_size, replace=replacements)
		indices.append(idx)

	indices = np.array(indices)

	ans = []

	for i in range(n_subsets):
		ans.append((X[indices][i], y[indices][i]))
	
	return ans




X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
n_subsets = 3
replacements = False
print(get_random_subsets(X, y, n_subsets, replacements))

