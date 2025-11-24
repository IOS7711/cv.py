import cv2
import numpy as np

# 1. 读取图片并提取整体掩码
img = cv2.imread("try.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 2. 合并所有元素为整体大轮廓
merge_kernel = np.ones((15, 15), np.uint8)
merged_mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, merge_kernel)

# 3. 对整体轮廓向外膨胀（膨胀的范围=描边与本体的间距）
gap_kernel = np.ones((15, 15), np.uint8)  # 15×15的核→间距约15像素
expanded_mask = cv2.dilate(merged_mask, gap_kernel, iterations=1)  # 向外扩张得到间距区域

# 4. 提取扩张后的轮廓（即描边的位置）
contours, _ = cv2.findContours(expanded_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 绘制带间距的红色粗描边
result = img.copy()
cv2.drawContours(result, contours, -1, (0, 0, 255), thickness=4)  # thickness=描边粗细

cv2.imshow("Stroke with Gap", result)
cv2.waitKey(0)
cv2.imwrite("try_stroke_with_gap.jpg", result)