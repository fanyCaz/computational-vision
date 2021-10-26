import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import grey_conversion as grey_cv
import utils
import normalize

def getHistogram()
  print("histogram")

def main()
  img = cv.imread("mina_cortada.png")
  grey_img = grey_cv.convert_to_greyscale(img)
  getHistogram()

if __name__ == '__main__':
  main()
