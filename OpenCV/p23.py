import cv2
import numpy as np

image=cv2.imread('square.png') #square.png
cv2.imshow('square',image)
cv2.waitKey(0)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,30,200)
cv2.imshow('Canny Edges',edged)
cv2.waitKey(0)

_,contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contourin',edged)
cv2.waitKey(0)

print('Number of contours found:'+str(len(contours)))
cv2.drawContours(image,contours,-1,(0,255,0),3)

cv2.imshow('Contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


