import numpy as np
import math
import cv2 as cv
import pysnooper
import utils

#PIXEL[row][column]
# print(img[0][0])

# RGB Red Green Blue
# OPENCV retrieves Blue Green Red
#RED VALUE
# print(img[0,0,2])

# Grey Conversion formula
# G = fr*R + fg*G + fb*B
# Pregunta: ¿siempre se hace un floor o se hace un redondeo de acuerdo al decimal?
# Siempre se trunca el valor para que no salga de los límites.
def convert_to_greyscale(image):
  grey_matrix = []
  grey_dict = {}
  red_freq = 1/3
  green_freq = 1/3
  blue_freq = 1/3
  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: math.trunc(blue_freq*pixel[0] + green_freq*pixel[1] + red_freq*pixel[2]),row))
    grey_matrix.append(row_pixels)
    grey_dict[i] = row_pixels
  greyscale = np.array(grey_matrix)
  utils.save_matrix('greyscale.json', grey_dict)
  return greyscale

img = cv.imread('../mina.jpeg')
grey_img = convert_to_greyscale(img)
cv.imwrite("mina_grey.png",grey_img)
