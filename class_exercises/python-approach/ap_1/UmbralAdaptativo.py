
import numpy as np
import cv2

gray = cv2.imread('makise.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('ESCALA GRISES', gray)

# umbral fijo
_, dst1 = cv2.threshold(gray, 96, 255, cv2.THRESH_BINARY)

cv2.imshow('umbral fijo', dst1)

# umbral adaptable
gray = cv2.medianBlur(gray, 5)
dst2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('umbral adaptable', dst2)

cv2.waitKey(0)
