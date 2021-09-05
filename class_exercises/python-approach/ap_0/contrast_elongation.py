import numpy as np
import cv2 as cv
import grey_conversion as grey_cv
import utils

def contrast_elongation(image, betha, gamma):
  elongated_matrix = []
  elongated_dict = []

  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: pixel * gamma + betha, row))
    elongated_matrix.append(row_pixels)
    elongated_dict.append(row_pixels)
  elongated = np.array(elongated_matrix)
  return elongated

img = cv.imread('../mina.jpeg')
grey_img = grey_cv.convert_to_greyscale(img)
beta = utils.input_normalized("Ingresa el valor beta")
gamma = utils.input_normalized("Ingresa el valor gamma",[0,2])
# PREGUNTA: GAMMA ES VALOR FLOTANTE??
elonged_img = contrast_elongation(grey_img,beta,gamma)
cv.imwrite("mina_elonged.png", elonged_img)
