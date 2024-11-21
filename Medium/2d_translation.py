import numpy as np
def translate_object(points, tx, ty):
	for point in points:
		point[0] += tx
		point[1] += ty
	return points
