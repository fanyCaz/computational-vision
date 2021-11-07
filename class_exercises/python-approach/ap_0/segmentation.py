import cv2 as cv
import numpy as np
from utils import print_matrix, input_normalized
import grey_conversion as grey_cv

#c_i current i
#c_j current j
def getAvailableNeighbours(image,c_i,c_j,alread_used):
  available = []
  no_rows = len(image)
  no_columns = len(image[0])
  # row search
  #esto podría ser un lambda
  for i in range(c_i-1,c_i+2):
    for j in range(c_j-1,c_j+2):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      if is_in_range and [i,j] not in alread_used:
        available.append([i,j])
  return available

def getNexPivot(image,alread_used):
  #search for next pixel not used
  #quitar el enumerate e irse por range mejor para que solo recorra numeros
  for row in range(0,len(image)):
    for column in range(0,len(image[0])):
      if [row,column] not in alread_used:
        return [row,column]

"""
  El arreglo available debe permanecer como vacío
    al principio de cada iteración.
  En el vecindario se pone el valor de shade del pivote
  El pivot es la posición del pivote actual
"""
def segment_image(image,alpha_cut):
  segmented_matrix = image
  no_rows = len(image)
  no_columns = len(image[0])
  sum_matrix = 0
  used = []
  total_sum = no_rows * no_columns
  while sum_matrix != total_sum:
    print(f"suma {sum_matrix} multi {total_sum}")
    if sum_matrix == 0:
      pivot = [0,0]
    else:
      pivot = getNexPivot(image,used)
    row = pivot[0]
    column = pivot[1]
    value_pivot = image[row,column]
    available = []
    available = getAvailableNeighbours(image,row,column,used)
    i = 0
    # Agrega los vecinos mientras va buscando
    if len(available) > 0:
      while i < len(available):
        pixel = available[i]
        current_pixel = image[pixel[0],pixel[1]]
        if abs(current_pixel - value_pivot) <= alpha_cut and pixel not in used:
          used.append([pixel[0],pixel[1]])
          available = available + getAvailableNeighbours(image,pixel[0],pixel[1],used)
          segmented_matrix[pixel[0],pixel[1]] = value_pivot
          sum_matrix += 1
          del available[i]
        i = i + 1
  segmented_matrix = np.array(segmented_matrix)
  return segmented_matrix

if __name__ == '__main__':
  alpha_cut = input_normalized('Ingresa el valor de corte: ')
  #grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128],[10,19,11,10,12]])
  image_name = "ajedrez.jpeg"
  img = cv.imread(image_name)
  grey_img = grey_cv.convert_to_greyscale(img)
  print_matrix(image_name+'_before_segmented_matrix.csv', grey_img)
  segmented_image = segment_image(grey_img,alpha_cut)
  print_matrix(image_name+'_segmented_matrix.csv', segmented_image)
  cv.imwrite(image_name+"segmented_matrix.png", segmented_image)
