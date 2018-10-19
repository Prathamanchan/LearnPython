import cv2
import numpy as np

image=cv2.imread("image.jpg")
zeros=np.zeros(image.shape[:2],dtype="uint8")
B,G,R= cv2.split(image)

cv2.imshow("RED",cv2.merge([zeros,zeros,R]))
cv2.imshow("GREEN",cv2.merge([zeros,G,zeros]))
cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))

cv2.waitKey()
cv2.destroyAllWindows()

