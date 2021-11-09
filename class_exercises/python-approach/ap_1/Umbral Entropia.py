# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:48:19 2019
Entropy Method
@author: yun
"""
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
 
def Entropy(gray):
    p = [] # Probabilidad gris
    
    H_last = 0 # Entropía total de la última H
    best_k = 0 # Mejor umbral
    hist = cv2.calcHist ([gray], [0], None, [256], [0,256]) # 255 * 1 matriz de histograma gris
    for i in range(256):
        p.insert(i,hist[i][0]/gray.size)
    for k in range(256):
        H_b = 0 # entropía del negro, la cantidad promedio de información en primer plano
        H_w = 0 # La entropía del blanco, la cantidad promedio de información de fondo
        for i in range(k):
            if p[i] != 0:
                H_b = H_b - p[i]*math.log(2,p[i])
        
        for i in range(k,256):
            if p[i] != 0:
                H_w = H_w - p[i]*math.log(2,p[i])
           
        H = H_b + H_w
        if H>H_last:
            H_last = H
            best_k = k
      
    return H,best_k
 
 
if __name__ == "__main__":
    img = cv2.imread ('leina.jpg') # Leer imagen (BGR)
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY) #Gire la imagen en escala de grises
    H,best_k = Entropy(gray)
    print(H,best_k)
    ret,thresh1=cv2.threshold(gray,best_k,255,cv2.THRESH_BINARY)
    cv2.imshow("histogram", thresh1)