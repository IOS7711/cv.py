import cv2

# 读取彩色图（默认BGR格式，包含蓝、绿、红三个通道）
image = cv2.imread("try.jpg")
#OpenCV中将彩色图转为标准灰度图的核心操作
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ## 关键：自动融合三通道生成标准灰度图
cv2.imshow("绘画和", gray_image)  # 显示最终灰度图
cv2.waitKey(0)
cv2.destroyAllWindows()
