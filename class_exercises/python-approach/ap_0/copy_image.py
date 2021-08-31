import numpy as np
import cv2 as cv
import grey_conversion as grey_cv
import utils

def copy_image(image):
  copied_image = image
  return copied_image

img = cv.imread("../mina.jpeg")
grey_img = grey_cv.convert_to_greyscale(img)
copied_image = copy_image(grey_img)
cv.imwrite("mina_copied.png", copied_image)
