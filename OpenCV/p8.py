import cv2
import numpy as np

img=cv2.imread('image.jpg')
rotated_image=cv2.transpose(img)

cv2.imshow('Rotated Image',rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()
