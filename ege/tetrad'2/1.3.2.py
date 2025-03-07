import numpy as np

matrix = np.zeros((5, 5), dtype=int)


for i in range(5):
    matrix[i, :] = np.arange(5)

print(matrix)
