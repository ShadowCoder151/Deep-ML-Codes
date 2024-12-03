import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	ih, iw = input_matrix.shape
	kh, kw = kernel.shape
	
	oh = ((ih - kh + 2 * padding) // stride) + 1
	ow = ((iw - kw + 2 * padding) // stride) + 1

	output_matrix = []

	image = np.pad(input_matrix, pad_width=padding)
	ih, iw = image.shape
	
	for i in range(0, ih - kh + 1, stride):
		C = []
		for j in range(0, iw - kw + 1, stride):
			S = float(np.sum(kernel * image[i:i + kh, j:j + kw]))
			C.append(S)
		output_matrix.append(C)


	return output_matrix

input_matrix = np.array([
    [1., 2., 3., 4., 5.],
    [6., 7., 8., 9., 10.],
    [11., 12., 13., 14., 15.],
    [16., 17., 18., 19., 20.],
    [21., 22., 23., 24., 25.],
])
kernel = np.array([
    [.5, 3.2],
    [1., -1.],
])
padding, stride = 2, 2

output = simple_conv2d(input_matrix, kernel, padding, stride)
print(output)