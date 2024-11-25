from collections import Counter

def confusion_matrix(data):
	conf = [[0] * 2 for _ in range(2)]
	
	for a, b in data:
		conf[1 - a][1 - b] += 1
	return conf
	
	
	
