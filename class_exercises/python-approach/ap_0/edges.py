import cv2 as cv
import numpy as np
from utils import print_matrix, input_normalized
import grey_conversion as grey_cv
from umbral import umbral_selection as u_binario
from colors import init_colors
from random import randrange as rand
import copy

#c_i current i
#c_j current j
def getAvailableNeighbours(image,c_i,c_j,alread_used):
  available = []
  no_rows = len(image)
  no_columns = len(image[0])
  # row search
  for i in range(c_i-1,c_i+2):
    for j in range(c_j-1,c_j+2):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      #if is_in_range and [i,j] not in alread_used:
      if is_in_range:
        available.append([i,j])
  return available

def isBorder(image,pixel,c_i,c_j,alpha_cut):
  no_rows = len(image)
  no_columns = len(image[0])
  for i in range(c_i-1,c_i+2):
    for j in range(c_j-1,c_j+2):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      #is > alpha_cut because the next pixel isnt part of the neighbourhood
      # the current_pixel is
      if is_in_range and abs(pixel - image[i,j]) > alpha_cut:
        return True
  return False

def pointIsWithinThreshold(image,pixel,c_i,c_j,grosor,threshold):
  no_rows = len(image)
  no_columns = len(image[0])
  for i in range(c_i-grosor,c_i+(grosor+1)):
    for j in range(c_j-grosor,c_j+(grosor+1)):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      if is_in_range and abs(pixel - image[i,j]) <= threshold:
        return True
  return False

def getNexPivot(image,alread_used,last_i):
  #search for next pixel not used
  print(f"last i {last_i}")
  for row in range(last_i,len(image)):
    for column in range(0,len(image[0])):
      if [int(row),int(column)] not in alread_used:
        return [row,column]

def cleanMatrix(image):
  clean = []
  for row in image:
    row_pixels = list(map(lambda pixel: [255,255,255],row))
    clean.append(row_pixels)
  clean = np.array(clean)
  return clean

"""
  El arreglo available debe permanecer como vacío
    al principio de cada iteración.
  En el vecindario se pone el valor de shade del pivote
  El pivot es la posición del pivote actual
"""
def segment_image(image,alpha_cut,original):
  colors = init_colors()
  colors_size = len(colors)
  segmented_matrix = copy.deepcopy(image)
  border_matrix = copy.deepcopy(image)
  no_rows = len(image)
  no_columns = len(image[0])
  sum_matrix = 0
  used = []
  total_sum = no_rows * no_columns
  pivot = [0,0]
  neighbours_count = 0
  borders = {}
  borders[neighbours_count] = []
  while sum_matrix != total_sum:
    print(f"+ {sum_matrix} * {total_sum}")
    if sum_matrix == 0:
      pass
    else:
      pivot = getNexPivot(image,used,pivot[0])
      borders[neighbours_count] = []
    row = pivot[0]
    column = pivot[1]
    value_pivot = image[row,column]
    available = []
    available = getAvailableNeighbours(image,row,column,used)
    i = 0
    color_iteration = rand(0,colors_size)
    # Agrega los vecinos mientras va buscando
    if len(available) > 0:
      while i < len(available):
        pixel = available[i]
        current_pixel = image[pixel[0],pixel[1]]
        if abs(current_pixel - value_pivot) <= alpha_cut and pixel not in used:
          used.append([pixel[0],pixel[1]])
          available = available + getAvailableNeighbours(image,pixel[0],pixel[1],used)
          segmented_matrix[pixel[0],pixel[1]] = int(value_pivot)
          sum_matrix += 1
          del available[i]
          if isBorder(image,current_pixel,pixel[0],pixel[1],alpha_cut):
            borders[neighbours_count].append( [pixel[0],pixel[1]] )
          ## COLOR IN IMAGE
            original[pixel[0],pixel[1]] = colors[color_iteration]
            border_matrix[pixel[0],pixel[1]] = 1
        i = i + 1
    neighbours_count += 1
  print(f"Cantidad de vecindarios: {neighbours_count}")
  segmented_matrix = np.array(segmented_matrix)
  border_matrix = np.array(border_matrix)
  print_matrix('borders_segmented_matrix.csv', border_matrix)
  ### BORDERS
  return segmented_matrix, original

def test():
  alpha_cut = 10
  #grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128],[10,19,11,10,12]])
  grey_img = np.array([[10,15,16,25,45],[30,18,70,80,110],[40,50,60,90,110]])
  segmented_image = segment_image(grey_img,alpha_cut,grey_img)
  print(segmented_image)

def prod():
  alpha_cut = input_normalized('Ingresa el valor de corte: ',[1,254])
  image_name = "figuras.jpeg"
  print(f"Imagen {image_name}")
  img = cv.imread(image_name)
  grey_img = grey_cv.convert_to_greyscale(img)
  binarizar = True
  if binarizar:
    grey_img = u_binario(grey_img,85)
  segmented_image,coloured = segment_image(grey_img,alpha_cut,img)
  printFiles = True
  if printFiles:
    print_matrix(image_name+'_before_segmented_matrix.csv', grey_img)
    print_matrix(image_name+'_segmented_matrix.csv', segmented_image)
    cv.imwrite(image_name+"_segmented_matrix.png", segmented_image)
    cv.imwrite(image_name+"_colored_segmented_matrix.png", coloured)

if __name__ == '__main__':
  #test()
  prod()
