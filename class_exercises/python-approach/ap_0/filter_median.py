import numpy as np
import cv2 as cv
import math
import grey_conversion as grey_cv
import utils
import normalize

def median_filter(image):
  filtered_matrix = []

  sorted_img = np.sort(image,axis=None)
  #print(np.median(sorted_img))
  median = np.median(sorted_img)
  mean = np.mean(sorted_img)
  print(f"Median value: {median}")

  for i,row in enumerate(image):
    row_pixels = list(map(lambda pixel: median if ((abs(mean - pixel)*100)/mean) > 7 else pixel, row))
    filtered_matrix.append(row_pixels)
  filtered = np.array(filtered_matrix)
  return filtered

image_name = "bosque_cortado.png"
img = cv.imread(image_name)
image_name = image_name.replace('.','')
grey_img = grey_cv.convert_to_greyscale(img)
#cv.imwrite("old_photo_grey.png",grey_img)
median_filtered_img = median_filter(grey_img)
utils.print_matrix(image_name+"_median_filter.csv",median_filtered_img)
cv.imwrite(image_name+"_median_filter.png",median_filtered_img)
