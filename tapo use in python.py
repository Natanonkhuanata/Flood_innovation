import cv2
url = "rtsp://C320ws:729513846@10.99.6.13:554/stream1"  #RTSP URL ที่มาจากกล้องเพื่อเป็นเส้นทางสู้การเปิดกล้อง
cap = cv2.VideoCapture(url)
while True:
    ret,frame = cap.read()
    cv2.imshow('Output', frame)
    if cv2.waitKey(1) &  0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()