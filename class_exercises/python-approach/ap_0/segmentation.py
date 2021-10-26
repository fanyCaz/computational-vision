import cv2 as cv
import numpy as np

class PivotFound(Exception): pass

#c_i current i
#c_j current j
def getAvailableNeighbours(image,c_i,c_j,alread_used):
  available = []
  no_rows = len(image)
  no_columns = len(image[0])
  #print(f"no rows {no_rows} no cols {no_columns}")
  # row search
  for i in range(c_i-1,c_i+2):
    for j in range(c_j-1,c_j+2):
      is_in_range = i >= 0 and j >= 0 and i < no_rows and j < no_columns
      if is_in_range and [i,j] not in alread_used:
        available.append([i,j])
        #print("valor en get available")
        #print([i,j])
  return available

def getNexPivot(image,alread_used):
  try:
    for row,pixel in enumerate(image):
      for column,val in enumerate(pixel):
        if [row,column] not in alread_used:
          raise PivotFounded
  except:
    print("Siguiente pivote")
    print(row,column)
    return [row,column]

def findNeighbourhood(image,new_matrix,c_i,c_j,alread_used,pivot,alpha_cut):
  available = []
  available = getAvailableNeighbours(image,c_i,c_j,alread_used)
  i = 0
  while len(available) > 0 and i < len(available):
    pixel = available[i]
    current_pixel = image[pixel[0],pixel[1]]
    if abs(current_pixel - pivot) <= alpha_cut and pixel not in used:
      used.append([pixel[0],pixel[1]])
      available = available + getAvailableNeighbours(image,pixel[0],pixel[1],used)
      neighbour[pivot].append([pixel[0],pixel[1]])
      new_matrix[pixel[0],pixel[1]] = pivot
    i = i + 1
    del available[i]  #remove the past value
  return new_matrix,alread_used

def main():
  colors = np.array([255,0,0])
  alpha_cut = 10
  grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128]])
  i = 0
  j = 0
  pivot = grey_img[i,j]
  segmented_matrix = grey_img
  """
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
  print("PIXELES OCUPADOS")
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
  #Aqui como ya encontraste el siguiente pivote, puedes hacer lo de arriba de nuevo, asi que hay que ponerlo en funcion, pero primero prueba que si funcione aqui
  #used = []
  
  pivot = grey_img[row,column]
  neighbour[pivot] = []
  available = []
  available = getAvailableNeighbours(grey_img,row,column,used)
  i = 0
  while len(available) > 0 and i < len(available):
    pixel = available[i]
    current_pixel = grey_img[pixel[0],pixel[1]]
    if abs(current_pixel - pivot) <= alpha_cut and pixel not in used:
      used.append([pixel[0],pixel[1]])
      available = available + getAvailableNeighbours(grey_img,pixel[0],pixel[1],used)
      neighbour[pivot].append([pixel[0],pixel[1]])
      segmented_matrix[pixel[0],pixel[1]] = pivot
    i = i + 1
    del available[i]
  print("en vecindario")
  print(neighbour[pivot])
  print("USADOS")
  print(used)
  print("Matriz segmentada")
  print(segmented_matrix)
  # SIGUIENTE VUELTA
  print("SIGUIENTE VUELTA")
  """
  """
    El arreglo available debe permanecer como vacío
    al principio de cada iteración.
    En el vecindario se pone el valor de shade del pivote
    El pivot es la posición del pivote actual
  """
  neighbour = {}
  no_rows = len(grey_img)
  no_columns = len(grey_img[0])
  sum_matrix = 0
  used = []
  while sum_matrix != (no_rows * no_columns):
    print(f"suma {sum_matrix} multi {no_rows * no_columns}")
    
    #se está atorando aquí
    if sum_matrix == 0:
      pivot = [0,0]
    else:
      pivot = getNexPivot(grey_img,used)
      #pivot_position = getNexPivot(grey_img,used)
      #pivot = grey_img[pivot_position[0], pivot_position[1]]
    print(f"pivote actual {pivot} ")
    row = pivot[0]
    column = pivot[1]
    value_pivot = grey_img[row,column]
    pivots = []
    pivots.append(value_pivot)
    neighbour[value_pivot] = []
    available = []
    available = getAvailableNeighbours(grey_img,row,column,used)
    i = 0
    while len(available) > 0 and i < len(available):
      pixel = available[i]
      current_pixel = grey_img[pixel[0],pixel[1]]
      if pivot == [4,3]:
        print(current_pixel)
        print(value_pivot)
      if abs(current_pixel - value_pivot) <= alpha_cut and pixel not in used:
        used.append([pixel[0],pixel[1]])
        available = available + getAvailableNeighbours(grey_img,pixel[0],pixel[1],used)
        neighbour[value_pivot].append([pixel[0],pixel[1]])
        segmented_matrix[pixel[0],pixel[1]] = value_pivot
        sum_matrix += 1
      i = i + 1
      #del available[0]
    print("Usados")
    print(used)
    print("Matriz segmentada")
    print(segmented_matrix)

if __name__ == '__main__':
  main()
