import numpy as np

def create_chessboard_matrix(size):
  matrix = np.zeros((size, size), dtype=int) 
  matrix[::2, ::2] = 1 
  matrix[1::2, 1::2] = 1 
  return matrix


chessboard = create_chessboard_matrix(8)


print(chessboard)
