import cv2
import numpy as np

# 1. 读取图片（替换为你的图片路径，和代码放同一文件夹即可）
img = cv2.imread("try.jpg")

# 2. 生成全黑背景图（和原图尺寸/格式一致）
red_channel = np.zeros_like(img)

# 3. 只保留红通道：把原图红通道细节填到全黑图的红通道
red_channel = img[:,:,2]

# 4. 显示结果（按任意键关闭窗口）
cv2.imshow("yuan tu", img)
cv2.imshow("dan hong", red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()