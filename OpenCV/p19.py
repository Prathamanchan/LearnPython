import cv2
import numpy as np

image=cv2.imread('image.jpg',0)
cv2.imshow('Orginal',image)

ret,thresh1=cv2.threshold
