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
def segment_image(image,alpha_cut,original,name):
  colors = init_colors()
  colors_size = len(colors)
  segmented_matrix = copy.deepcopy(image)
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
        i = i + 1
    neighbours_count += 1
  print(f"Cantidad de vecindarios: {neighbours_count}")
  segmented_matrix = np.array(segmented_matrix)

  ### BORDERS
  #findRansac(original, borders,colors,alpha_cut,image)
  cv.imwrite("borders_colored_segmented_matrix.png", original)
  # Clean matrix to use in HOUGH
  H = copy.deepcopy(image)
  h_matrix = []
  for row in H:
    #row_pixels = list(map(lambda pixel: 0 if pixel < umbral else 255,row))
    row_pixels = list(map(lambda pixel: 0,row))
    h_matrix.append(row_pixels)
  h_matrix = np.array(h_matrix)

  #Binarizar imagen
  grey_img = u_binario(segmented_matrix,85)
  cv.imwrite("binary_borders_colored_segmented_matrix.png", segmented_matrix)

  grey_img = copy.deepcopy(image)
  #RANSAC and HOUGH
  m_max = 0
  border_grosor = 1
  umbral = 85
  lines = {}
  for i,border in enumerate(borders):
    M = 0
    lines[i] = []
    for k in borders[i]:
      if pointIsWithinThreshold(grey_img,grey_img[k[0],k[1]],k[0],k[1],border_grosor,umbral):
        M += 1
        h_matrix[k[0],k[1]] = h_matrix[k[0],k[1]] + 1
        lines[i].append([k[0],k[1]])
      if M > m_max:
        m_max = M
  coloured = copy.deepcopy(original)
  for i,line in enumerate(lines):
    color_it = rand(0,len(colors))
    for k in lines[i]:
      coloured[k[0],k[1]] = colors[color_it]

  cv.imwrite(name+"liness_2_colored_segmented_matrix.png", coloured)
  print("Print values of hough HoughTransform")
  print_matrix(name+'hough.csv',h_matrix)
  lines_coloured = []
  for i,row in enumerate(h_matrix):
    color_it = rand(0,len(colors))
    row_pixels = list(map(lambda pixel: 0 if pixel >= 1 else 255,row))
    lines_coloured.append(row_pixels)
  lines_coloured = np.array(lines_coloured)
  cv.imwrite(name+"liness_hough_1_colored_segmented_matrix.png", lines_coloured)
  return segmented_matrix, original

def test():
  alpha_cut = 10
  #grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128],[10,19,11,10,12]])
  grey_img = np.array([[10,15,16,25,45],[30,18,70,80,110],[40,50,60,90,110]])
  segmented_image = segment_image(grey_img,alpha_cut,grey_img)
  print(segmented_image)

def prod():
  alpha_cut = input_normalized('Ingresa el valor de corte: ',[1,254])
  image_name = "corner.png"
  print(f"Imagen {image_name}")
  img = cv.imread(image_name)
  grey_img = grey_cv.convert_to_greyscale(img)
  binarizar = True
  if binarizar:
    grey_img = u_binario(grey_img,85)
  segmented_image,coloured = segment_image(grey_img,alpha_cut,img,image_name)
  printFiles = False
  if printFiles:
    print_matrix(image_name+'_before_segmented_matrix.csv', grey_img)
    print_matrix(image_name+'_segmented_matrix.csv', segmented_image)
    cv.imwrite(image_name+"_segmented_matrix.png", segmented_image)
    cv.imwrite(image_name+"_colored_segmented_matrix.png", coloured)

if __name__ == '__main__':
  #test()
  prod()
