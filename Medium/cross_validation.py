import numpy as np

def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)

    indices = np.arange(len(data))
    np.random.shuffle(indices)
    data_1 = data[indices]

    fold_size = len(data) // k
    folds = []

    for i in range(k):
        start = i * fold_size
        end = start + fold_size
        
        test = data_1[start:end]
        train = np.concatenate((data_1[:start], data_1[end:]), axis=0)

        folds.append([test, train])
    return folds


data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
k = 5

print(cross_validation_split(data=data, k=k))