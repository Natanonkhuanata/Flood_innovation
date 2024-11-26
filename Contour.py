import cv2

img = cv2.imread("scale.jpg")
img_resize = cv2.resize(img,(1000,800))
gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
thresh , result = cv2.threshold(gray,215,255,cv2.THRESH_BINARY)
gray_blur = cv2.GaussianBlur(gray,(15,15),1)

contours , hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#print(len(contours))

cv2.imshow("Outpuut",gray_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()