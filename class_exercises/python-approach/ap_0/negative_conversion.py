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
  utils.print_matrix('negative.txt', negative)
  return negative

img = cv.imread("mina_cortada.png")
grey_img = grey_cv.convert_to_greyscale(img)
negative_img = negative_image(grey_img)
cv.imwrite("mina_negative.png", negative_img)
