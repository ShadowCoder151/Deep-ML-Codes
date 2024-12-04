import numpy as np

class SimpleRNN:
	def __init__(self, input_size, hidden_size, output_size):
		"""
		Initializes the RNN with random weights and zero biases.
		"""
		self.hidden_size = hidden_size
		self.W_xh = np.random.randn(hidden_size, input_size)*0.01
		self.W_hh = np.random.randn(hidden_size, hidden_size)*0.01
		self.W_hy = np.random.randn(output_size, hidden_size)*0.01
		self.b_h = np.zeros((hidden_size, 1))
		self.b_y = np.zeros((output_size, 1))

	def forward(self, x):
		# h_t = [np.zeros((self.hidden_size, 1))]
		# for inp in x:
		# 	a = np.dot(self.W_xh, inp) + np.dot(self.W_hh, h_t) + self.b_h
		# 	h_t = np.tanh(a)
		# 	o = np.dot(self.W_hy, h_t) + self.b_y

		# return o, h_t
		h_t = np.zeros((self.hidden_size, 1))
		hidden_states = []
		outputs = []

		# print(self.W_xh.shape, x[0].shape)
		# print(self.W_hh.shape, h_t.shape)
		# print(self.b_h.shape)

		# print('----')
		# print(self.W_hy.shape, h_t.shape, self.b_y.shape)

		for index ,inp in enumerate(x):
			# print(f'Loop {index + 1}')

			a = self.W_xh @ inp.reshape(-1, 1) + self.W_hh @ h_t + self.b_h
			h_t = np.tanh(a)
			
			o = self.W_hy @ h_t + self.b_y
			# print(o)
			hidden_states.append(h_t)
			outputs.append(o)

		return np.array(outputs), hidden_states
	
	def backward(self, x, y, learning_rate):
		outputs, hidden_states = self.forward(x)

		dW_xh = np.zeros_like(self.W_xh)
		dW_hh = np.zeros_like(self.W_hh)
		dW_hy = np.zeros_like(self.W_hy)
		db_h = np.zeros_like(self.b_h)
		db_y = np.zeros_like(self.b_y)

		dh_next = np.zeros((self.hidden_size, 1))

		for t in reversed(range(len(x))):
			dy = (outputs[t] - y[t].reshape(-1, 1))
			
			dW_hy += np.dot(dy, hidden_states[t].T)
			db_y += dy

			dh = np.dot(self.W_hy.T, dy) + dh_next
			da = (1 - hidden_states[t] ** 2) * dh  

			dW_xh += np.dot(da, x[t].reshape(1, -1).T)  
			dW_hh += np.dot(da, hidden_states[t - 1].T)
			db_h += da

			dh_next = np.dot(self.W_hh.T, da)

		self.W_xh -= learning_rate * dW_xh / len(x)
		self.W_hh -= learning_rate * dW_hh / len(x)
		self.W_hy -= learning_rate * dW_hy / len(x)
		self.b_h -= learning_rate * db_h / len(x)
		self.b_y -= learning_rate * db_y / len(x)
	


np.random.seed(42) 

input_sequence = np.array([[1.0], [2.0], [3.0], [4.0]])
expected_output = np.array([[2.0], [3.0], [4.0], [5.0]])

rnn = SimpleRNN(input_size=1, hidden_size=5, output_size=1)

# Train the RNN over multiple epochs
for epoch in range(100):
    output, _ = rnn.forward(input_sequence)
    rnn.backward(input_sequence, expected_output, learning_rate=0.01)

print(output)