import numpy as np

def divide_on_feature(X, feature_i, threshold):
	ans = [[], []]
	for i in range(len(X)):
		if X[i][feature_i] >=threshold:
			ans[0].append(X[i])
		else:
			ans[1].append(X[i])

	return ans


X = np.array([[1, 2], 
				[3, 4], 
				[5, 6], 
				[7, 8], 
				[9, 10]])
feature_i = 0
threshold = 5
print(divide_on_feature(X, feature_i, threshold))