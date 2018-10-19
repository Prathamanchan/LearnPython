import cv2
import numpy as np

def get_contour_areas(contours):

	all_areas=[]
	for cnt in contours:
		area=cv2.contourArea(cnt)
		all_areas.append(area)
	return all_areas

image=cv2.imread('square.png')
original_image=image

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,50,200)
cv2.imshow('1-canny Edges',edged)
cv2.waitKey(0)

_,contours,hierarchy= cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print(" Number of contours found ",len(contours))

print "contour Areas before sorting"
print get_contour_areas(contours)

sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)

print "Contour Areas after sorting"
print get_contour_areas(sorted_contours)

for c in sorted_contours:
	cv2.drawContours(original_image,[c],-1,(255,0,0),3)
	cv2.waitKey(0)
	cv2.imshow('COntour by Area',original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
