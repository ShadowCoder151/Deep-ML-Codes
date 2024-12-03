import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))

class LSTM:
	def __init__(self, input_size, hidden_size):
		self.input_size = input_size
		self.hidden_size = hidden_size

		# Initialize weights and biases
		self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

		self.bf = np.zeros((hidden_size, 1))
		self.bi = np.zeros((hidden_size, 1))
		self.bc = np.zeros((hidden_size, 1))
		self.bo = np.zeros((hidden_size, 1))

	def forward(self, x, initial_hidden_state, initial_cell_state):
		for inp in x:
			inp = inp.reshape(-1, 1)
			prev = np.vstack([initial_hidden_state, inp])
			fg = sigmoid(self.Wf @ prev + self.bf)
			ig = sigmoid(self.Wi @ prev + self.bi)
			ct_ = np.tanh(self.Wc @ prev + self.bc)
			initial_cell_state = fg * initial_cell_state + ig * ct_
			
			ot = sigmoid(self.Wo @ prev + self.bo)
			initial_hidden_state = ot * np.tanh(initial_cell_state)
		
		return ot, initial_hidden_state, initial_cell_state

input_sequence = np.array([[0.1, 0.2], [0.3, 0.4]])
initial_hidden_state = np.zeros((2, 1))
initial_cell_state = np.zeros((2, 1))

lstm = LSTM(input_size=2, hidden_size=2)
# Set weights and biases for reproducibility
lstm.Wf = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
lstm.Wi = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
lstm.Wc = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
lstm.Wo = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
lstm.bf = np.array([[0.1], [0.2]])
lstm.bi = np.array([[0.1], [0.2]])
lstm.bc = np.array([[0.1], [0.2]])
lstm.bo = np.array([[0.1], [0.2]])

outputs, final_h, final_c = lstm.forward(input_sequence, initial_hidden_state, initial_cell_state)

print(final_h)