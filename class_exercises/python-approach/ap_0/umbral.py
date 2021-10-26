import numpy as np
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize

def umbral_selection(image,umbral):
  umbral_matrix = []

  for i,row in enumerate(image):
    row_pixels = list(map(lambda pixel: 0 if pixel < umbral else 255,row))
    umbral_matrix.append(row_pixels)
  under_umbral = np.array(umbral_matrix)
  matrix_name = f"umbral_{umbral}.csv"
  utils.print_matrix(matrix_name,under_umbral)
  return under_umbral

if __name__ == '__main__':
  print("Umbral")
  img = cv.imread('bosque_1_grey.png')
  grey_img = grey_cv.convert_to_greyscale(img)
  umbral = utils.input_normalized("Ingresa el valor de umbral de interés: ",[1,254])
  umbral_img = umbral_selection(grey_img, umbral)
  name_img = f"bosque_1_umbral_{umbral}.png"
  cv.imwrite(name_img,umbral_img)
