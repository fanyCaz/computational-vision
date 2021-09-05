import numpy as np
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize
import pysnooper

def contrast_elongation(image, betha, gamma):
  elongated_matrix = []
  elongated_dict = []

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: pixel * gamma + betha, row))
    elongated_matrix.append(np.trunc(row_pixels))
    elongated_dict.append(row_pixels)
  elongated = np.array(elongated_matrix)
  utils.print_matrix('contrast_elongation.txt',elongated)
  elongated = normalize.normal(elongated,'contrast_normalized_elongation.txt')
  return elongated

img = cv.imread('mina_cortada.png')
grey_img = grey_cv.convert_to_greyscale(img)
beta = utils.input_normalized("Ingresa el valor beta : ")
gamma = utils.input_normalized("Ingresa el valor gamma : ",[0,2])
# PREGUNTA: GAMMA ES VALOR FLOTANTE??
# Si, gamma es flotante
elonged_img = contrast_elongation(grey_img,beta,gamma)
cv.imwrite("mina_elonged.png", elonged_img)
