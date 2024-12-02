import numpy as np
from collections import defaultdict
from collections import Counter
import math

def compute_tf_idf(corpus, query):
	S = 0
	idf = {}
	term = {}

	N = len(corpus)

	for q in query:
		s = sum(q in c for c in corpus)
		idf[q] = math.log((N + 1) / (s + 1)) + 1 if s > 0 else 0
	
	for i, c in enumerate(corpus):
		term[i] = Counter(c)
	
	# print(term)
	# print(idf)

	ans = []
	for i in range(N):
		S = []
		for q in query:
			S.append(round(term[i][q] * idf[q] / len(corpus[i]), 5))
		ans.append(S)
	
	return ans


corpus = [
    ["the", "cat", "sat", "on", "the", "mat"],
    ["the", "dog", "chased", "the", "cat"],
    ["the", "bird", "flew", "over", "the", "mat"]
]
query = ["cat"]

print(compute_tf_idf(corpus, query))
