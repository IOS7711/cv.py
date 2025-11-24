import cv2
import numpy as np

# 1. 读取图片（确保try.jpg和代码同文件夹）
img = cv2.imread("try.jpg")
# 2. 获取图片尺寸+设定旋转中心（图片中心）
h, w = img.shape[:2]  # 核心：提取图片的高度和宽度
center = (w//2, h//2)
# 3. 生成旋转矩阵（向左45度=逆时针45度，缩放1.0不变形）
rot_mat = cv2.getRotationMatrix2D(center, 45, 1.0)
# 4. 执行旋转（自动填充背景，直接输出完整图片）
rotated_img = cv2.warpAffine(img, rot_mat, (w, h))
# 5. 保存+显示结果
cv2.imwrite("rotated_try.jpg", rotated_img)
cv2.imshow("test.6.jpg", rotated_img)
cv2.waitKey(0)  # 按任意键关闭窗口
cv2.destroyAllWindows()