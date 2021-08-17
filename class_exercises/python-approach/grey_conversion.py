import numpy as np
import math
import cv2 as cv

img = cv.imread('similar.png')

print(img)

#PIXEL[row][column]
print(img[0][0])

# RGB Red Green Blue
#RED VALUE
print(img[0][0][0])

# G = fr*R + fg*G + fb*B
# Pregunta: ¿siempre se hace un floor o se hace un redondeo de acuerdo al decimal?
print(math.trunc(20.8))
print(int(img[0][0][0] * 1/3))

grey_matrix = []
# Pregunta: ¿si les llama frequency o porque f?
general_frequency = 1/3
red_freq = 1/3
green_freq = 1/3
blue_freq = 1/3

for i,row in enumerate(img):
  row_pixels = list(map(lambda pixel: math.trunc(red_freq*pixel[0] + green_freq*pixel[1] + blue_freq*pixel[2]), row))
  #print(row_pixels)
  grey_matrix.append(row_pixels)

#print(grey_matrix)
