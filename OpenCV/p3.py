import cv2

image=cv2.imread('image.jpg')

B,G,R=cv2.split(image)
print B.shape

cv2.imshow("RED",R)
cv2.imshow("GREEN",G)
cv2.imshow("BLUE",B)


cv2.waitKey()
cv2.destroyAllWindows()

merged=cv2.merge([B,G,R])
cv2.imshow("Merged",merged)

merged=cv2.merge([B+100,G+100,R+100])
cv2.imshow("Merged With Blue Amplified",merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
