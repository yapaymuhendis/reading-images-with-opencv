import cv2

path = cv2.imread("images/test.PNG")


cv2.imshow("test", path)


cv2.waitKey(0)
cv2.destroyAllWindows() # herhangi bi tuşa basıldığında programı kapatıyor.




