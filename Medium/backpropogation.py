import numpy as np

def error(y_true, y_pred):
	return np.mean((y_true - y_pred) ** 2)

def sigmoid(z):
	return 1 / (1 + np.exp(-z))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	E = []
	for _ in range(epochs):
		X = features @ initial_weights + initial_bias
		Z = sigmoid(X)

		E.append(error(labels, Z))

		e = (Z - labels) * Z * (1 - Z)
		change_W = 2 * features.T @ e / len(labels)
		change_B = 2 * np.mean(e)

		initial_weights -= learning_rate * change_W
		initial_bias -= learning_rate * change_B

	return np.round(initial_weights, 4), np.round(initial_bias, 4), np.round(np.array(E), 4)