import torch
from Segment_anything_model import sam_model_registry, SamPredictor
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# โหลดโมเดล
sam_checkpoint = "path_to_your_model/sam_vit_b_01ec64.pth"
model_type = "vit_b"  # เปลี่ยนตามโมเดลที่ใช้
device = "cuda" if torch.cuda.is_available() else "cpu"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

# โหลดภาพ
image_path = "path_to_your_image.jpg"
image = np.array(Image.open(image_path))

# ตั้งค่า SAM predictor
predictor = SamPredictor(sam)
predictor.set_image(image)

# เลือกพิกัดจุดสำหรับวัตถุที่ต้องการแยก
input_point = np.array([[300, 400]])  # ตัวอย่างจุดในภาพ
input_label = np.array([1])  # 1 หมายถึง foreground

# ประมวลผล
masks, scores, _ = predictor.predict(point_coords=input_point, point_labels=input_label, multimask_output=True)

# แสดงผล
plt.figure(figsize=(10, 10))
plt.imshow(image)
for i, mask in enumerate(masks):
    plt.contour(mask, colors=[f"C{i}"])
plt.axis("off")
plt.show()
