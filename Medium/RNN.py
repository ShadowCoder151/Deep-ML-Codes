import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
	input_sequence, initial_hidden_state, Wx, Wh, b = [np.array(param) for param in [input_sequence, initial_hidden_state, Wx, Wh, b]]

	for inp in input_sequence:
		a = np.dot(Wx, inp) + np.dot(Wh, initial_hidden_state) + b
		initial_hidden_state = np.tanh(a)
	
	return np.round(initial_hidden_state, 4)





input_sequence = [[1.0], [2.0], [3.0]]
initial_hidden_state = [0.0]
Wx = [[0.5]]  # Input to hidden weights
Wh = [[0.8]]  # Hidden to hidden weights
b = [0.0]
print(rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b))