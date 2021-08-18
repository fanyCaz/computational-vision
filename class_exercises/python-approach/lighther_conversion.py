import numpy as np
import math
import cv2 as cv
import pysnooper

img = cv.imread('similar.png')

print(img)

#PIXEL[row][column]
print(img[0][0])

# RGB Red Green Blue
# This will return Blue Green Red
#BLUE VALUE
print(img[0][0][0])

# G = fr*R + fg*G + fb*B
# Pregunta: ¿siempre se hace un floor o se hace un redondeo de acuerdo al decimal?
#print(math.trunc(20.8))
#print(int(img[0][0][0] * 1/3))

### COPY

grey_img = img

grey_matrix = []
# Pregunta: ¿si les llama frequency o porque f?
general_frequency = 1/3
red_freq = 1/3
green_freq = 1/3
blue_freq = 1/3

# Change the colors to be blue green red
for i,row in enumerate(img):
  row_pixels = list(map(lambda pixel: math.trunc(red_freq*pixel[2] + green_freq*pixel[1] + blue_freq*pixel[0]), row))
  #print(row_pixels)
  grey_matrix.append(row_pixels)

def avoid_overflow(image_matrix):
  # solo con una sola operación?
  # Se hace una normalización, para el valor relativo
  print( np.amin(image_matrix) )
  print( np.amax(image_matrix) )
  return

#@pysnooper.snoop()
def change_image(imagen,matrix):
  for i, row in enumerate(imagen):
    for j, pixel in enumerate(row):
      #imagen.itemset((i,j),matrix[i][j])
      imagen[i,j] = matrix[i][j]
  return imagen

def lighten_image(imagen,matrix):
  for i, row in enumerate(imagen):
    for j, pixel in enumerate(row):
      print(matrix[i][j] + 295)
      imagen[i,j] = matrix[i][j] + 295
      # Tengo que bajarlo un nivel más para que pueda ser usado como matriz de numpy y no como un objeto normalizado de cv2 la libreria
      print(f"imagen : {imagen[i,j]}")
  return imagen

#new_image = change_image(grey_img,grey_matrix)

new_image = lighten_image(grey_img,grey_matrix)
avoid_overflow(new_image)
#cv.imwrite("new_imagen.png",new_image)
#print(grey_matrix)
# FALTA HACER LA CONVERSIÓN PARA CONVERTIR LA MATRIZ A UNA IMÁGEN

# EN UN PROGRAMA DIFERENTE HACER PARA EL USUARIO EL ACLARADO, COPIADO Y NEGATIVO
