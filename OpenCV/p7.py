import cv2
import numpy as np

image=cv2.imread('image.jpg')
height,width=image.shape[:2]

rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,1)

rotated_image=cv2.warpAffine(image,rotation_matrix,(width,height))

cv2.imshow('Rotated Image',rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
