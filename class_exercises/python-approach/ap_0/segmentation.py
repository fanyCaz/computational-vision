import cv2 as cv
import numpy as np
import utils
import grey_conversion as grey_cv

class PivotFound(Exception): pass

#c_i current i
#c_j current j
def getAvailableNeighbours(image,c_i,c_j,alread_used):
  available = []
  no_rows = len(image)
  no_columns = len(image[0])
  #print(f"no rows {no_rows} no cols {no_columns}")
  # row search
  for i in range(c_i-1,c_i+2):
    for j in range(c_j-1,c_j+2):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      if is_in_range and [i,j] not in alread_used:
        available.append([i,j])
        #print("valor en get available")
        #print([i,j])
  return available

def getNexPivot(image,alread_used):
  #search for next pixel not used
  try:
    for row,pixel in enumerate(image):
      for column,val in enumerate(pixel):
        if [row,column] not in alread_used:
          raise PivotFounded
  except:
    print("Siguiente pivote")
    print(row,column)
    return [row,column]

def segment_image(image,alpha_cut):
  i = 0
  j = 0
  pivot = image[i,j]
  segmented_matrix = image
  """
    El arreglo available debe permanecer como vacío
      al principio de cada iteración.
    En el vecindario se pone el valor de shade del pivote
    El pivot es la posición del pivote actual
  """
  no_rows = len(image)
  no_columns = len(image[0])
  sum_matrix = 0
  used = []
  while sum_matrix != (no_rows * no_columns):
    print(f"suma {sum_matrix} multi {no_rows * no_columns}")
    if sum_matrix == 0:
      pivot = [0,0]
    else:
      pivot = getNexPivot(image,used)
    row = pivot[0]
    column = pivot[1]
    value_pivot = image[row,column]
    pivots = []
    pivots.append(value_pivot)
    available = []
    available = getAvailableNeighbours(image,row,column,used)
    i = 0
    # Agrega los vecinos mientras va buscando
    while len(available) > 0 and i < len(available):
      pixel = available[i]
      current_pixel = image[pixel[0],pixel[1]]
      if abs(current_pixel - value_pivot) <= alpha_cut and pixel not in used:
        used.append([pixel[0],pixel[1]])
        available = available + getAvailableNeighbours(image,pixel[0],pixel[1],used)
        segmented_matrix[pixel[0],pixel[1]] = value_pivot
        sum_matrix += 1
      i = i + 1
  segmented_matrix = np.array(segmented_matrix)
  return segmented_matrix

def main():
  alpha_cut = utils.input_normalized('Ingresa el valor de corte: ')
  #alpha_cut = 10
  #grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128]])
  image_name = "mina_cortada.png"
  img = cv.imread(image_name)
  grey_img = grey_cv.convert_to_greyscale(img)
  segmented_image = segment_image(grey_img,alpha_cut)
  utils.print_matrix('segmented_matrix.csv', segmented_image)
  
  cv.imwrite("segmented_matrix.png", segmented_image)

if __name__ == '__main__':
  main()
