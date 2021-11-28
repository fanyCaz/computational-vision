

import numpy as np
import cv2 as cv
from scipy import stats
import grey_conversion as grey_cv
import utils
import normalize

def noise_removal(image, alpha_cut):
  noiseless_matrix = []

  flatten_img = image.flatten()
  median = np.median(sorted_img)
  #Aqui le aplicaria un unmbral con la moda y a partir de ahi aplicaria el :
  # mode if ((abs(mean-pixel)*100/mean)) > 7 else pixel ???

  for row in image:
    row_pixels = list(map(lambda pixel: median if ((abs(median-pixel)*100/mode)) > 60 else pixel, row))
    noiseless_matrix.append(row_pixels)
  noiseless = np.array(noiseless_matrix)
  return noiseless

img = cv.imread("salt_pepper.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
width = img.shape[1]
height = img.shape[0]
print("Elige el espacio de la imagen a cortar")
print(f"El ancho de la imagen es {width} y la altura es {height}")
a,b,c,d = utils.choose_image_section(width,height)
cut_img = grey_img[c:d,a:b]
noisless_img = noise_removal(cut_img)
utils.print_matrix("salt_pepper.csv", noisless_img)
cv.imwrite("salt_noiseless_salt_pepper.png", noisless_img)
