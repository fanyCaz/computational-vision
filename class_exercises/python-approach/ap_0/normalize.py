import numpy as np
import math
import utils

def normal(matrix,name_matrix):
  max_value = matrix.max()
  min_value = matrix.min()
  if min_value < 0:
    new_matrix = down_to_up(matrix,min_value)
    utils.print_matrix(name_matrix,new_matrix)
    return normal(new_matrix,name_matrix)
  elif max_value > 255:
    new_matrix = up_to_down(matrix,max_value)
    utils.print_matrix(name_matrix,new_matrix)
    return normal(new_matrix,name_matrix)
  else:
    return matrix

def up_to_down(matrix, max_value):
  print("Necesita normalizar hacia abajo porque tiene mas de 255 en pixeles")
  print(f"Valor excesivo: {max_value}")
  new_matrix = []
  for row in matrix:
    row_pixels = list(map(lambda pixel: math.trunc(pixel * 255 / max_value),row))
    new_matrix.append(row_pixels)
  new_matrix = np.array(new_matrix)
  return new_matrix

def down_to_up(matrix, min_value):
  print("Necesita normalización hacia arriba porque tiene negativos")
  print(f"Valor negativo: {min_value}")
  new_matrix = []
  for row in matrix:
    row_pixels = list(map(lambda pixel: math.trunc(pixel - min_value),row))
    new_matrix.append(row_pixels)
  new_matrix = np.array(new_matrix)
  return new_matrix
