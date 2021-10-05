import numpy as np
import cv2 as cv
import grey_conversion as grey_cv
import utils
import pysnooper

def search_grid(image,i,j,pivot,alpha):
  neighbours = []
  east = abs(image[i,j+1] - pivot) <= alpha
  south = abs(image[i+1,j] - pivot) <= alpha
  neast = abs(image[i+1,j+1] - pivot) <= alpha
  if east:
    neighbours.append({'pixel':image[i,j+1],'i': i, 'j': j+1})
  if south:
    neighbours.append({'pixel':image[i+1,j],'i': i+1, 'j': j})
  if neast:
    neighbours.append({'pixel':image[i+1,j+1],'i': i+1, 'j': j+1})
  return neighbours
# Se tiene que hacer un buscador, una funcion que busque en las orillas de la imagen, y asi pueda guardar los vecinos que quedan
def calculate_neighbour(image,alpha):
  pivot = image[0,0]
  i = 0
  j = 0
  print(f"pivote _ {pivot}")
  neighbours = {}
  neighbours[pivot] = []
  neighbours[pivot].append( search_grid(image,i,j,pivot,alpha) )
  neighbours[pivot] = np.array(neighbours[pivot]).flatten()

  print("First iteration")
  print(neighbours)

  next_i = neighbours[pivot][0]['i'] 
  next_j = neighbours[pivot][0]['j'] 
  #search_grid(image,next_i,next_j,pivot,alpha)
  neighbours[pivot] = np.append( neighbours[pivot], search_grid(image,next_i,next_j,pivot,alpha) )
  neighbours[pivot] = np.array(neighbours[pivot]).flatten()
  """ 
  for i,row in enumerate(image):
    for j, pixel in enumerate(row):
      current_pixel = pixel
      try:
        if abs(image[i,j+1] - pivot) <= 10:
          neighbours[pivot].append({'pixel':image[i,j+1],'i': i, 'j': j+1})
      except:
        pass
  """
  print("Final iteration")
  print(neighbours)
  return

#img = cv.imread("mina_cortada.png")
#grey_img = grey_cv.convert_to_greyscale(img)
# HAY QUE PEDIR AL USUARIO EL FACTOR DE ARRIBA-ABAJO DEL PIVOTE
grey_img = np.array([[78,86,88,97,104],[85,92,97,103,111],[93,98,103,109,114],[100,105,111,116,120],[105,112,117,122,128]])
cut_value = 10
neighboured_img = calculate_neighbour(grey_img,cut_value)
#cv.imwrite("mina_neighbours.png",neighboured_img)
