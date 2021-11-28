import numpy as np
import cv2 as cv
from utils import print_matrix, input_normalized
import grey_conversion as grey_cv
from umbral import umbral_selection as u_binario
from colors import init_colors
import copy

def circle(image):
  img = cv.imread(cv.samples.findFile('figures.jpeg'))
  gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  edges = cv.Canny(img,50,150,apertureSize = 3)
  lines = cv.HoughLines(edges,1,np.pi/180,150)
  for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
  cv.imwrite("circulos.png",img)

def main():
  name_img = 'ajedrez_corto.jpeg'
  img = cv.imread(name_img)
  grey_img = grey_cv.convert_to_greyscale(img)
  circles_img = circle(grey_img)
  #cv.imwrite(name_img+"_circles.png",circles_img)

if __name__ == '__main__':
  main()