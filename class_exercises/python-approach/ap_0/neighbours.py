import numpy as np
import cv2 as cv
import grey_conversion as grey_cv
import utils
import pysnooper

def search_grid(image,i,j,pivot,alpha):
  neighbours = []
  n = e = s = w = ne = se = sw = nw = False
  #North, East, South, West, and derivades
  if i - 1 > 0 or j - 1 > 0:
    n = abs(image[i-1,j] - pivot) <= alpha
    w = abs(image[i,j-1] - pivot) <= alpha
    ne = abs(image[i-1,j+1] - pivot) <= alpha
    sw = abs(image[i+1,j-1] - pivot) <= alpha
    nw = abs(image[i-1,j-1] - pivot) <= alpha
  e = abs(image[i,j+1] - pivot) <= alpha
  s = abs(image[i+1,j] - pivot) <= alpha
  se = abs(image[i+1,j+1] - pivot) <= alpha

  if n:
    neighbours.append([ i, j+1])
  if s:
    neighbours.append([i+1, j])
  if w:
    neighbours.append([i,j-1])
  if e:
    neighbours.append([])
  return neighbours
# Se tiene que hacer un buscador, una funcion que busque en las orillas de la imagen, y asi pueda guardar los vecinos que quedan
def calculate_neighbour(image,alpha):
  pivot = image[0,0]
  i = 0
  j = 0
  print(f"pivote _ {pivot}")
  #search_grid(image,i,j,pivot,alpha)
  #used = []
  #neighbours = {}
  #id_neighbourhood = 0
  """
  neighbours[id_neighbourhood] = [] 
  neighbours[id_neighbourhood].append({'i': i,'j': j})
  neighbours[id_neighbourhood].append( search_grid(image,i,j,pivot,alpha) )
  print(neighbours)
  neighbours[id_neighbourhood] = np.array(neighbours[id_neighbourhood]).flatten()
  """
    #se le debe aplicar un color a cada vecindario que no se repita y random,o crear una lista de 100 colores disponibles
  print("First iteration")
  print(neighbours)
  #checar sólo los habilitados
  #checar si está en usados o no
  #habilita el pedazo de matriz que ocupa
  #flag los elementos que ya han sido obtenidos
  """
  next_i = neighbours[id_neighbourhood][0]['i'] 
  next_j = neighbours[id_neighbourhood][0]['j'] 
  #search_grid(image,next_i,next_j,pivot,alpha)
  neighbours[id_neighbourhood] = np.append( neighbours[id_neighbourhood], search_grid(image,next_i,next_j,pivot,alpha) )
  neighbours[id_neighbourhood] = np.array(neighbours[id_neighbourhood]).flatten()
  """
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
