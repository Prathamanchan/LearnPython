import cv2
import numpy as np

image=cv2.imread('image.jpg')
height,width=image.shape[:2]

start_row,start_col=int(height*.25),int(width*.25)
end_row,end_col=int(height*.75),int(width*.75)

cropped= image[start_row:end_row,start_col:end_col]

cv2.imshow('Original',image)
cv2.waitKey()

cv2.imshow('Cropped',cropped)
cv2.waitKey()

cv2.destroyAllWindows()
