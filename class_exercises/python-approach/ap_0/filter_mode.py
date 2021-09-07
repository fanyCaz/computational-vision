import numpy as np
import cv2 as cv
from scipy import stats
import grey_conversion as grey_cv
import utils

def mode_filter(image):
  filtered_matrix = []

  sorted_img = np.sort(image,axis=None)
  mode = stats.mode(sorted_img)[0][0]
  mean = np.mean(sorted_img)
  print(f"Mode value: {mode}")

  for i,row in enumerate(image):
    row_pixels = list(map(lambda pixel: mode if ((abs(mean - pixel)*100/mean)) > 10 else pixel,row))
    filtered_matrix.append(row_pixels)
  filtered = np.array(filtered_matrix)
  utils.print_matrix("filter_mode.txt",filtered)
  return filtered

img = cv.imread("old_photo.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
mode_filtered_img = mode_filter(grey_img)
cv.imwrite("old_photo_mode_filtered.png",mode_filtered_img)
