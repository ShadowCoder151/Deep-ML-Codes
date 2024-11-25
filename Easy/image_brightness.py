from collections import defaultdict

def calculate_brightness(img):
	if img == []:
		return -1
	m, n = len(img), len(img[0])
	H = defaultdict(int)
	
	for i in range(len(img)):
		count = 0
		for j in range(len(img[i])):
			if 0 <= img[i][j] <= 255:
				H[len(img[i])] += img[i][j]
			else:
				return -1
	# print(H)
	return -1 if len(H) > 1 else H[len(img[0])] / (m * n)
			
			
	
	
