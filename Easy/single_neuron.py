import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	m, n = len(features), len(features[0])
	probabilities = [0 for _ in range(m)]
	
	for i in range(m):
		S = 0
		for j in range(n):
			S += features[i][j] * weights[j]
		
		S += bias
		probabilities[i] = round(1 / (1 + math.exp(-S)), 4)
		
	mse = (sum((labels[i] - probabilities[i]) ** 2 for i in range(m))) / m
	mse = round(mse, 4)
	
	return probabilities, mse