def minor(matrix, row, col):
    M = []
    for i in range(len(matrix)):
        if i == row:
            continue  
        X = []
        for j in range(len(matrix)):
            if j == col:
                continue  
            X.append(matrix[i][j])
        M.append(X)
    return M


def det(matrix):
    if len(matrix) == 2:  # Base case for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    ans = 0
    for j in range(len(matrix[0])):
        ans += (-1) ** (j) * matrix[0][j] * det(minor(matrix, 0, j))
    return ans


def determinant_4x4(matrix: list[list[int | float]]) -> float:
    return det(matrix)
	


def determinant_4x4(matrix: list[list[int | float]]) -> float:
    return det(matrix, 1)
	


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(determinant_4x4(a))