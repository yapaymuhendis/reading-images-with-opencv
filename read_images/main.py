import cv2

# We use the imread command to read the picture to where the picture is.
path = cv2.imread("images/test.PNG")

#We use the imshow command to show the file it is reading.
cv2.imshow("test", path)

#If we do not use the waitkey command, the image will not stay on the screen.
cv2.waitKey(0)

cv2.destroyAllWindows() 
