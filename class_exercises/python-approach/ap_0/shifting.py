import numpy as np
from scipy import stats
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize

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
  gradient = []
  for i,pixel in enumerate(image[0]):
    if i == len(image[0]) - 1:
      pass
    else:
      gradient.append(image[0][i+1]/ pixel)
  min_gradient_value = np.where(gradient == np.amin(gradient))[0][0]
  ## obtener el numero de columna que va a ser el pivote, lo siguiente falta obtener el index
  pivot_column = image[min_gradient_value] -1 if image[min_gradient_value] - 1  is not None else image[min_gradient_value] + 1 
  print(pivot_column)
  return

#img = cv.imread('mina_cortada.png')
#grey_img = grey_cv.convert_to_greyscale(img)
#choosen_type = utils.input_normalized("Elige el tipo de Shifting : 1) Horizontal, 2) Vertical",[1,2])
choosen_type = 1
grey_img = np.array( [[34,76,128,167],[56,88,136,175],[79,96,145,188],[91,121,167,194]] )
shifted_img = []
img_name = ""
if choosen_type == 1:
  shifted_img = horizontal_shifting(grey_img)
  img_name = f"mina_shifted_horizontal.png"
elif choosen_type == 2:
  shifted_img = vertical_shifting(grey_img)
  img_name = f"mina_shifted_vertical.png"

#print(img_name)
#cv.imwrite(img_name,shifted_img)
