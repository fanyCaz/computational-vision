import numpy as np
import cv2 as cv
import grey_conversion as grey_cv
import utils

def negative_image(image):
  negative_matrix = []
  negative_dict = {}

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: 255 - pixel, row))
    negative_matrix.append(row_pixels)
    negative_dict[i] = [ str(j) for j in row_pixels ]
  negative = np.array(negative_matrix)
  utils.save_matrix('negative.json', negative_dict)
  return negative

img = cv.imread("../mina.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
negative_img = negative_image(grey_img)
cv.imwrite("mina_negative.png", negative_img)
