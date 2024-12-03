import numpy as np

# def hv(dimension, seed):
# 	np.random.seed(seed)
# 	return np.random.choice([-1, 1], size=dimension)


# def create_row_hv(row, dim, random_seeds):
# 	ans = np.zeros(shape=(dim, ))
	
# 	for feature in random_seeds:
# 		h1 = hv(dim, random_seeds[feature])
# 		h2 = hv(dim, random_seeds[feature])

# 		X = h1 * h2
# 		ans += X
	
# 	ans = np.sign(ans)
# 	return ans

def create_row_hv(row, dim, random_seeds):
	ans = np.zeros(shape=(dim,))

	for feature in random_seeds:
		np.random.seed(random_seeds[feature])
		h1 = np.random.choice([-1, 1], size=dim)
		h2 = np.random.choice([-1, 1], size=dim)  
		X = h1 * h2
		ans += X
		
	ans = np.where(ans >= 0, 1, -1)
	return ans

row = {"FeatureA": "value1", "FeatureB": "value2"}
dim = 5
random_seeds = {"FeatureA": 42, "FeatureB": 7}
print(create_row_hv(row, dim, random_seeds))