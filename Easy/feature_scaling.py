import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mn = np.mean(data, axis=0)
	sd = np.std(data, axis=0)
	
	standardized_data = (data - mn) / sd
	
	MX = np.max(data, axis=0)
	MN = np.min(data, axis=0)
	
	normalized_data = (data - MN) / (MX - MN)
	return standardized_data, normalized_data