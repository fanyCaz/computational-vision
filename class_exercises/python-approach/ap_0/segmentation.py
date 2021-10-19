import cv2 as cv
import numpy as np


def main():
  print("am")
  colors = '255,0,0'
  alpha_cut = 10
  grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128]])
  pivot = grey_img[0,0]
  segmented_matrix = grey_img
  print(pivot)
  available = []
  available.append([0,1])
  available.append([1,0])
  available.append([1,1])
  print(available)
  neighbour = []
  # Agrega los vecinos mientras va buscando
  for i,pixel in enumerate(available):
    print(grey_img[pixel[0],pixel[1]])
    current_pixel = grey_img[pixel[0],pixel[1]]
    if abs(current_pixel - pivot) <= alpha_cut:
      print("si entra")
      available.append([pixel[0]+1,pixel[1]+1])
      available.append([pixel[0],pixel[1]+1])
      available.append([pixel[0]+1,pixel[1]])
      print(segmented_matrix[pixel[0],pixel[1]])
      segmented_matrix[pixel[0],pixel[1]] = colors

  print(segmented_matrix)

if __name__ == '__main__':
  main()
