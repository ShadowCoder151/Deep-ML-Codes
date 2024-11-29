import numpy as np

def matrix_image(A):
    OG = A.copy()
    m, n = A.shape
    row, col = 0, 0
    ans = []

    while row < m and col < n:
        pivot = A[row][col]
        if pivot == 0:
            col += 1
        else:
            for k in range(row + 1, m):
                div = A[k][col] / pivot
                A[k] = A[k] - div * A[row]
            
            ans.append(OG[:, col])
            row += 1
            col += 1
    
    ans = np.array(ans).T
    return ans
            


print(matrix_image(np.array([[1, 0], [0, 1]])))



        