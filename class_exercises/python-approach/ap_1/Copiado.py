import cv2
from PIL import Image
import numpy as np
from numpy.core.records import array

def escalaGrises():
    #para abrir la imagen
    BA = int(input("Escoge un número del 0 al 255 para indicar lo aclarado de la imagen"))
    arr_image= Image.open("makise.jpg")
    # Necesitamos convertir la imagen a un array
    array_image = np.array(arr_image)
    #Creando array similar, sacamos dimensiones 0 dimensiones , 1 columnas 
    array_zeros = np.zeros((int(array_image.shape[0]),int(array_image.shape[1])))
    array_copia = np.zeros((int(array_image.shape[0]),int(array_image.shape[1])))
    for n in (range (array_image.shape[0])):
        for m in (range( array_image.shape[1])):
            # el arreglo estara representado como tridimencional porque
            #tiene 3 valores (RGB)
            R=0
            G=0
            B=0
            suma = 0
            
            for j in (range(array_image.shape[2])):
                #vamos a tener 3 condiciones para recorrer los valores de RGB y convertirlo
                # a escala de grises
                if j == 0:
                    #Formula para convertir a escala de grises 
                    R= array_image[n,m,j]* 0.3
                    suma = suma + R
                elif j == 1 : 
                    #Si entra aqui es Green
                    G= array_image[n,m,j]* 0.59
                    suma = suma + G
                else:
                    B= array_image[n,m,j]* 0.11
                    suma = suma + B
            array_zeros[n,m] = suma  + BA#Aqui puse el 50 como aclardo
            array_copia[n,m] =  array_zeros[n,m]
    #representando imagen
    cv2.imwrite("Aclarado.jpg",array_zeros)#Aqui cambie el nombre para hacer pruebas
    cv2.imwrite("CopiaAclarado.jpg",array_copia)
    
    print("Array ImageColor\n\n", array_image)
    arr_image2= Image.open("CopiaAclarado.jpg")
    array_image2 = np.array(arr_image2)
    arr_image3 = Image.open("Aclarado.jpg")
    array_image3 = np.array(arr_image3)
    #print("Array zeros\n\n", array_zeros)
    print("Array ImageCopiaAclarada:\n\n ", array_image2)
    print("Aclarado:\n\n", array_image3)
    variable = cv2.imread("CopiaAclarado.jpg",0)
    cv2.imshow('CopiaAclarado',variable)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
escalaGrises()     