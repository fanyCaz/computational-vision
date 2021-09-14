import numpy as np
import cv2 as cv
from scipy import stats
import grey_conversion as grey_cv
import utils
import pysnooper

def rank_order(image):
  filtered_matrix = []

  sorted_img = np.sort(image,axis=None)
  mean = np.mean(sorted_img)
  closer_to_mean = 300
  idx_closer_to_mean = 0
  print(len(sorted_img))

  for i,pixel in enumerate(sorted_img):
    sum_intensity = sum(list(map(lambda pxl: abs(pixel-pxl),sorted_img)))
    if sum_intensity < closer_to_mean:
      idx_closer_to_mean = i
      closer_to_mean = sum_intensity
  rank_value = sorted_img[idx_closer_to_mean]

  for row in image:
    row_pixels = list(map(lambda pixel: rank_value if ((abs(mean-pixel)*100/mean)) > 7 else pixel,row))
    filtered_matrix.append(row_pixels)
  filtered = np.array(filtered_matrix)
  return filtered


img = cv.imread("bosque_1.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
width = img.shape[1]
height = img.shape[0]
print("Elige el espacio de la imagen a cortar")
a,b,c,d = utils.choose_image_section(width,height)
#print(points)
# slicing is [y,x]
cut_img = grey_img[c:d,a:b]
cv.imwrite("bosque_cortado.png",cut_img)
#grey_img = np.array([[45,56,65],[70,81,84],[88,90,216]])
rank_filtered_img = rank_order(cut_img)
cv.imwrite("bosque_rank_filtered.png", rank_filtered_img)
