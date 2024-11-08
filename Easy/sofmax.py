import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	S = sum(math.exp(num) for num in scores)
	
	probabilities = [round(math.exp(num) / S, 4) for num in scores]
	return probabilities