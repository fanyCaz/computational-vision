import numpy as np
from scipy import stats
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize
import pysnooper

def horizontal_shifting(image):
  # Primero tiene que ver hacia donde va la luminosidad
  """
  max_values = np.amax(image, axis=1)
  indexes_maxs = []
  for i in max_values:
    indexes_maxs.append(np.where(image == i)[1][0])
  most_repeated_index = stats.mode(indexes_maxs)[0]
  dist = []k
  for i in image:
  """
  # la luminosidad esta hacia el lado donde el index de donde se encontraron los mayores valores estan
  # Pregunta: Se toma en cuenta cada una de las rows? o solo la de arriba y la de abajo, o solo la de arriba
  # lo que hice fue tomar el gradiente,
  # hay que hacer la matriz al reves primero, si se tiene que hacer de izquierda a derecha
  gradient = []
  for i,pixel in enumerate(image[0]):
    if i == len(image[0]) - 1:
      pass
    else:
      gradient.append(image[0][i+1]/ pixel)
  min_gradient_value = np.where(gradient == np.amin(gradient))[0][0]
  ## obtener el numero de columna que va a ser el pivote
  print(min_gradient_value)
  print(f"longitud imagen: {len(image[0]) - 1}")
  half_image_index = math.trunc(len(image[0])/2)
  print(half_image_index)
  pivot_column = []
  pivot_index = 0
  #if image[:,min_gradient_value+1:] is not None:
  if min_gradient_value < half_image_index: 
    pivot_column = image[:,min_gradient_value+1:]
    #pivot_index = min_gradient_value + 1
    pivot_index = 0
  else:
    pivot_column = image[:,min_gradient_value-1:]
    #pivot_index = min_gradient_value - 1
    pivot_index = len(image[0]) - 1

  print("Columna pivote")
  print(pivot_column)

  print("Index pivote")
  print(pivot_index)
  shifted_matrix = image
  new_matrix = []
  # flip los valores de luminosidad
  if pivot_index == len(image[0]) - 1:
    iterable = np.flipud(shifted_matrix.T)
    for j,column in enumerate(iterable):
      new_column = np.zeros(len(iterable[0]))
      if pivot_index != 0:
        new_column= iterable[j]
      else:
        for i,pixel in enumerate(column):
          new_value = math.trunc(new_matrix[j-1][i]*iterable[j-1][i]/pixel) 
          new_column[i] = new_value
      new_matrix.append(new_column)
  else:
    print("Entro a esta iteracion")
    #iterable = np.flipud(shifted_matrix.T)
    #iterable = np.fliplr(iterable)
    iterable = np.fliplr(shifted_matrix.T)
    utils.print_matrix('iteracion.txt',iterable)
    for j,column in enumerate(iterable):
      new_column = np.zeros(len(iterable[0]))
      if pivot_index == 0:
        new_column = iterable[len(iterable) - 1]
        pivot_index = None
      else:
        for i,pixel in enumerate(column):
          new_value = math.trunc(new_matrix[j-1][i]*iterable[j-1][i]/pixel)
          new_column[i] = new_value
      new_matrix.append(new_column)

  new_matrix = np.array(new_matrix)
  new_matrix = np.fliplr(new_matrix.T)
  utils.print_matrix('shifted.txt',new_matrix)
  new_matrix = normalize.normal(new_matrix,'shifted_normalized.txt')
  return new_matrix

img = cv.imread('mina_cortada.png')
grey_img = grey_cv.convert_to_greyscale(img)
#choosen_type = utils.input_normalized("Elige el tipo de Shifting : 1) Horizontal, 2) Vertical",[1,2])
choosen_type = 1
#grey_img = np.array( [[34,76,128,167],[56,88,136,175],[79,96,145,188],[91,121,167,194]] )
shifted_img = []
img_name = ""
if choosen_type == 1:
  shifted_img = horizontal_shifting(grey_img)
  img_name = f"mina_shifted_horizontal.png"
elif choosen_type == 2:
  shifted_img = vertical_shifting(grey_img)
  img_name = f"mina_shifted_vertical.png"

#print(img_name)
cv.imwrite(img_name,shifted_img)
