import cv2
import numpy as np

# 1. 读图片 + 转成“黑白灰”（灰度图）
img = cv2.imread("try.jpg")  # 读你要处理的图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把彩色图转成灰度图（只有黑、白、灰）
# 为啥转灰度？因为灰度图只有“亮度”一个属性，方便电脑判断“哪是背景”

# 2. 告诉电脑：“亮度高于240的都是背景”（关键步骤）
ret, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
# - 拿灰度图的每个像素比亮度：比240亮的（比如纯白、浅灰背景），标为“255（白色）”；
# - 比240暗的（比如主体、文字），标为“0（黑色）”；
# - 最后得到一张“掩码图”（mask）：背景是白色，主体是黑色（相当于给背景“打标签”）

# 3. 反转掩码图：背景变黑，主体变白
mask_inv = cv2.bitwise_not(mask)
# 为啥反转？因为后面要告诉电脑：“白色的地方要保留，黑色的地方要换黑背景”
# 反转后：掩码图里“主体”是白色，“背景”是黑色

# 4. 保留主体 + 背景换成黑色
foreground = cv2.bitwise_and(img, img, mask=mask_inv)  # 只留主体（掩码图白色的地方）
background_black = np.zeros_like(img)  # 造一张全黑的图（新背景）
result = cv2.bitwise_or(foreground, background_black)  # 把主体放在黑背景上
# 大白话：就像“把主体剪下来，贴到黑色的纸上”

# 5. 看结果
cv2.imshow("yuan tu", img)
cv2.imshow("xing tu", result)
cv2.waitKey(0)  # 保持窗口显示
cv2.destroyAllWindows()