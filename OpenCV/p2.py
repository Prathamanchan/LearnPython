import cv2
image=cv2.imread('image.jpg')
hsv_image= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image',hsv_image)
cv2.imshow('HUE Channel',hsv_image[:,:,0])
cv2.imshow('Saturation Channel',hsv_image[:,:,1])
cv2.imshow('Value Channel',hsv_image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()


