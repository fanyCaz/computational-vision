import cv2

image = cv2.imread('cut_tree2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for contour in cnts:
  epsilon = 0.01*cv2.arcLength(contour,True)
  approx = cv2.approxPolyDP(contour,epsilon,True)
  x,y,w,h = cv2.boundingRect(approx)

  if len(approx) > 10:
    cv2.putText(image,'Circulo', (x,y-5),1,1,(0,255,0),1)

  cv2.drawContours(image, [approx], 0, (0,255,0),2)
  #cv2.imshow('image',image)
  #cv2.waitKey(0)
cv2.imwrite('figures.png', image)