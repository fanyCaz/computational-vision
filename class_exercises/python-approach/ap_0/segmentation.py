import cv2 as cv
import numpy as np

class PivotFound(Exception): pass

def main():
  colors = np.array([255,0,0])
  alpha_cut = 10
  grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128]])
  i = 0
  j = 0
  pivot = grey_img[i,j]
  segmented_matrix = grey_img
  print(f"pivote: {pivot}")
  available = []
  available.append([0,1])
  available.append([1,0])
  available.append([1,1])
  pivots = []
  pivots.append(pivot)
  neighbour = {}
  neighbour[pivot] = []
  used = []
  used.append([0,0])
  # Agrega los vecinos mientras va buscando
  # Este for puede ser una función que reciba available y grey_img
  for i,pixel in enumerate(available):
    print(grey_img[pixel[0],pixel[1]])
    current_pixel = grey_img[pixel[0],pixel[1]]
    if abs(current_pixel - pivot) <= alpha_cut and pixel not in used:
      print("si entra")
      used.append([pixel[0],pixel[1]])
      available.append([pixel[0]+1,pixel[1]+1])
      available.append([pixel[0],pixel[1]+1])
      available.append([pixel[0]+1,pixel[1]])
      print(segmented_matrix[pixel[0],pixel[1]])
      neighbour[pivot].append([pixel[0],pixel[1]])

  print(neighbour[pivot])
  print( available[-1] in used )
  print(used)
  #search for next not used pixel
  try:
    for row,pixel in enumerate(grey_img):
      for column,val in enumerate(pixel):
        print(row,column)
        if [row,column] not in used:
          print(f"siguiente pivote: {grey_img[row,column]}")
          raise PivotFounded
  except:
    print(row,column)

  pivots.append(grey_img[row,column])
  print(pivots)
  #Aqui como ya encontraste el siguiente pivote, puedes hacer lo de arriba de nuevo, asi que hay que ponerlo en funcion, pero primero prueba que si funcione aqui
  print(segmented_matrix)
  used = []

if __name__ == '__main__':
  main()