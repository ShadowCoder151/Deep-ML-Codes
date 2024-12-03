import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
	return X @ W_q, X @ W_k, X @ W_v

softmax = lambda x: np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

def self_attention(Q, K, V):
	m, n = Q.shape
	score = softmax(Q @ K.T / np.sqrt(n))
	attention_output = score @ V
	return attention_output


X = np.array([[1, 0], [0, 1]])
W_q = np.array([[1, 0], [0, 1]])
W_k = np.array([[1, 0], [0, 1]])
W_v = np.array([[1, 2], [3, 4]])

Q, K, V = compute_qkv(X, W_q, W_k, W_v)
output = self_attention(Q, K, V)

print(output)