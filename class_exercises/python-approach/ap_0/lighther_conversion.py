import numpy as np
import math
import cv2 as cv
import pysnooper
import grey_conversion as grey_cv
import utils
import normalize

# Se hace una normalización, para el valor relativo

def lighten_image(image, betha):
  lighten_matrix = []

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: math.trunc(pixel + betha), row))
    lighten_matrix.append(row_pixels)
  lightened = np.array(lighten_matrix)
  utils.print_matrix('lightened.txt', lightened)
  lightened = normalize.normal(lightened, 'lightened_normalized.txt')
  return lightened

img = cv.imread("mina_cortada.png")
grey_img = grey_cv.convert_to_greyscale(img)
beta = utils.input_normalized("Ingresa el valor betha de intensidad: ")
lightened_img = lighten_image(grey_img, beta)
cv.imwrite("mina_ligthen.png", lightened_img)
