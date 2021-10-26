import numpy as np
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize

def negative_image(image):
  negative_matrix = []

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: 255 - pixel, row))
    negative_matrix.append(np.trunc(row_pixels))
  negative = np.array(negative_matrix)
  return negative

image_name = "bosque_cortado.png"
img = cv.imread(image_name)
grey_img = grey_cv.convert_to_greyscale(img)
negative_img = negative_image(grey_img)
utils.print_matrix(image_name+"_negativo.csv", negative_img)
cv.imwrite(image_name+"_negativo.png", negative_img)
