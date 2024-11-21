import numpy as np

def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)

    fold_size = int(np.ceil(len(data) / k))
    folds = []
    for i in range(k):
        start = i * fold_size
        end = start + fold_size
        test = data[start:end]
        train = np.concatenate((data[:start], data[end:]), axis=0)
        folds.append([train.tolist(), test.tolist()])
    return folds


data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
k = 5

print(cross_validation_split(data=data, k=k))