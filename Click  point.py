import cv2
import matplotlib.pyplot as plt
"""
# โหลดภาพ
image_path = "Flood01.jpg"  # ระบุ path ของภาพ
image = cv2.imread(image_path)

# แปลงเป็น Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ลด noise ด้วย Gaussian Blur
blurred = cv2.GaussianBlur(gray, (15,15),1)

# ใช้ Canny Edge Detection
threshold1 = 50  # ค่าขั้นต่ำ
threshold2 = 150  # ค่าสูงสุด
edges = cv2.Canny(blurred, threshold1, threshold2)

# แสดงผล
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # แสดงภาพสีใน Matplotlib
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Edges Detected (Canny)")
plt.imshow(edges, cmap="gray")  # แสดงภาพขาวดำ
plt.axis("off")

plt.show()

"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# โหลดภาพ
image_path = "new-img2.jpg"
image = np.array(Image.open(image_path))

# ฟังก์ชันสำหรับเก็บจุดคลิก
clicked_points = []

def onclick(event):
    # เก็บพิกัด x, y เมื่อคลิก
    x, y = int(event.xdata), int(event.ydata)
    clicked_points.append([x, y])
    print(f"Point clicked: ({x}, {y})")

# แสดงภาพและรอรับคลิก
fig, ax = plt.subplots()
ax.imshow(image)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

# พิกัดที่เลือก
print(f"Selected points: {clicked_points}")
