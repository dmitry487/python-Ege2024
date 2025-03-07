import numpy as np

size = 5  

matrix = np.zeros((size, size), dtype=int) 

matrix[0, :] = 1  
matrix[-1, :] = 1  
matrix[:, 0] = 1 
matrix[:, -1] = 1 
print(matrix)
