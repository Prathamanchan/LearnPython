import numpy as np
import cv2

image=cv2.imread('image.jpg')
dst=cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)

cv2.imshow('Fast Means Denosing',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
