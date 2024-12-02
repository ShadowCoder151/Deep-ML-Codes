import numpy as np

def hv(dimension, seed):
	np.random.seed(seed)
	return np.random.choice([-1, 1], size=dimension)


def create_row_hv(row, dim, random_seeds):
	ans = np.ones(shape=(dim, ))
	
	for feature in random_seeds:
		hyper = hv(dim, random_seeds[feature])
		ans = ans * hyper
	
	return ans

row = {"FeatureA": "value1", "FeatureB": "value2"}
dim = 5
random_seeds = {"FeatureA": 42, "FeatureB": 7}
print(create_row_hv(row, dim, random_seeds))