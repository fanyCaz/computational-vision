import numpy as np
import math
import cv2 as cv
import pysnooper
import utils
import normalize

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
  red_freq = 1/3
  green_freq = 1/3
  blue_freq = 1/3
  for i, row in enumerate(image):
    row_pixels = list(map(lambda pixel: math.trunc(blue_freq*pixel[0] + green_freq*pixel[1] + red_freq*pixel[2]),row))
    grey_matrix.append(row_pixels)
  greyscale = np.array(grey_matrix)
  greyscale = normalize.normal(greyscale, 'greyscale_normalized.txt')
  return greyscale

def main():
  image_name = "estrellas.jpeg"
  img = cv.imread(image_name)
  image_name = image_name.replace('.','')
  grey_img = convert_to_greyscale(img)
  utils.print_matrix(image_name+"_grey.csv", grey_img)
  cv.imwrite(image_name+"_grey.png",grey_img)

if __name__ == '__main__':
  main()
