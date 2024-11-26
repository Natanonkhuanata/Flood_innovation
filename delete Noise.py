import cv2
import numpy as np



img  = cv2.imread("Flood01.jpg")
img_resize = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
#Gaussian blur & Threshold
gray_blur = cv2.GaussianBlur(img_gray,(15,15),1)
#Adaptive Thresholding
Threshold = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,38)
kernel = np.ones((6,6),np.uint8)
clossing = cv2.morphologyEx(Threshold,cv2.MORPH_CROSS,kernel,iterations=5)
    
img_dilate = cv2.dilate(clossing,kernel,iterations=3)
img_Thre = cv2.erode(img_dilate,kernel,iterations=1)
thresh , result = cv2.threshold(img_Thre,215,255,cv2.THRESH_BINARY)   

contours , hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img_resize,contours,-1,(0,0,255),2)



cv2.imshow("Normal",clossing)
cv2.imshow("imgThe",img_resize)

    

cv2.waitKey(0)
cv2.destroyAllWindows()

    
    #contour,Heirachy = cv2.findContours(img_Thre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

"""
    for cn in contour:
        area = cv2.contourArea(cn)
        if area < 2000 or area > 3500:
            continue

        (x,y),(w,h),angle = rect = cv2.minAreaRect(cn)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.circle(img_resize,(int(x),int(y)),3,[0,0,255],-1)
        cv2.polylines(img_resize,[box],True,[255,0,0],2)
        cv2.rectangle(img_Thre,(x,y),(x+w,(y+h)),(0,255,0),2)
    cv2.imshow("Normal",img_resize)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
    
"""


"""
result = clossing.copy()
    contours,hierachy = cv2.findContours(result,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cn in contours:
        area = cv2.contourArea(cn)
        if area < 2000 or area < 35000:
            contours
        rectangle = cv2.fitEllipse(cn) 
        cv2.rectangle(img_resize,rectangle,(255,0,0),2)

        cv2.imshow("output",img_resize)

"""