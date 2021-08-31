import numpy as np
import math
import cv2 as cv
import pysnooper
import grey_conversion as grey_cv
import utils

# Se hace una normalización, para el valor relativo

def lighten_image(image, betha):
  #row_pixels = list(map(lambda pixel: pixel
  lighten_matrix = []
  lighten_dict = {}

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: pixel + betha, row))
    lighten_matrix.append(row_pixels)
    lighten_dict[i] = [ str(j) for j in row_pixels ]
  lightened = np.array(lighten_matrix)
  utils.save_matrix('lightened.json', lighten_dict)
  return lightened

img = cv.imread("../mina.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
beta = utils.input_normalized("Ingresa el valor betha de intensidad")
lightened_img = lighten_image(grey_img, beta)
cv.imwrite("mina_ligthen.png", lightened_img)
