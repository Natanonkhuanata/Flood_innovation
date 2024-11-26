import cv2
import numpy as np

# โหลดภาพด้วย OpenCV
image = cv2.imread("Flood01.jpg")
img_resize = cv2.resize(image,(1000,800))
gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

# ค้นหาจุดเด่นในภาพ (ตัวอย่างใช้ threshold)
_, thresh = cv2.threshold(gray,215, 255, cv2.THRESH_BINARY)
Threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,48)
kernel = np.ones((6,6),np.uint8)
clossing = cv2.morphologyEx(Threshold,cv2.MORPH_CROSS,kernel,iterations=5)
img_dilate = cv2.dilate(clossing,kernel,iterations=3)

# หา contours และจุดกลางของ contour ที่ใหญ่ที่สุด
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
M = cv2.moments(largest_contour)

center_x = int(M["m10"] / M["m00"])
center_y = int(M["m01"] / M["m00"])

input_point = np.array([[center_x, center_y]])  # พิกัดจุด
input_label = np.array([1])  # foreground

cv2.imshow("output",gray)
cv2.imshow("thresh",thresh)
cv2.imshow("ad",img_dilate)
cv2.waitKey(0)

#print(input_point)