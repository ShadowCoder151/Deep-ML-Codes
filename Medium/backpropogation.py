import numpy as np

def error(y_true, y_pred):
	return np.sum((y_true - y_pred) ** 2) / len(y_true)

def sigmoid(z):
	return 1 / (1 + np.exp(-z))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	E = []
	for _ in range(epochs):
		X = features @ initial_weights + initial_bias
		Z = sigmoid(X)

		E.append(error(labels, Z))

		e = (Z - labels) * Z * (1 - Z)
		change_W = features.T @ e
		change_B = np.mean(e)

		initial_weights = initial_weights - learning_rate * change_W
		initial_bias = initial_bias - learning_rate * change_B

	return np.round(initial_weights, 4), np.round(initial_bias, 4), np.round(np.array(E), 4)


features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
labels = np.array([1, 0, 0])
initial_weights = np.array([0.1, -0.2])
initial_bias = 0.0
learning_rate = 0.1
epochs = 2

print(train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs))

