import cv2
import random
def pepper_and_salt(img,percentage):
    num=int(percentage*img.shape[0]*img.shape[1])# Número de puntos de ruido de sal y pimienta
    random.randint(0, img.shape[0])
    img2=img.copy()
    for i in range(num):
        X=random.randint(0,img2.shape[0]-1)# Un número entero aleatorio desde 0 hasta la longitud de la imagen, porque es un intervalo cerrado, -1
        Y=random.randint(0,img2.shape[1]-1)
        if random.randint(0,1) ==0: # Probabilidad en blanco y negro 55 abierto
            img2[X,Y] = (255,255,255)#blanco
        else:
            img2[X,Y] =(0,0,0)#negro
    return img2
img=cv2.imread("makise.jpg")
img2 = pepper_and_salt(img,0.04)# 4 por ciento de ruido de sal y pimienta
cv2.imshow("Makise",img)
cv2.imshow("Makise_Sal_Pimienta",img2)
cv2.waitKey(0)

