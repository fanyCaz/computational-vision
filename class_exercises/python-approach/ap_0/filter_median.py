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
    row_pixels = list(map(lambda pixel: median if ((abs(mean - pixel)*100)/mean) > 10 else pixel, row))
    filtered_matrix.append(row_pixels)
  filtered = np.array(filtered_matrix)
  utils.print_matrix("filter_median.txt",filtered)
  return filtered

img = cv.imread("old_photo.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
#cv.imwrite("old_photo_grey.png",grey_img)
median_filtered_img = median_filter(grey_img)
cv.imwrite("old_photo_median_filtered.png",median_filtered_img)
