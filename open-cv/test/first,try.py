import cv2
import sys

# 从launch.json读取图片名（核心对接json参数）
image_path = sys.argv[1]

# 读取图片（OpenCV原生支持，无需其他库）
img = cv2.imread(image_path)

# 验证图片是否读取成功
if img is not None:
    # 弹出图片窗口（OpenCV自带窗口，无依赖）
    cv2.namedWindow("Image Display", cv2.WINDOW_NORMAL)  # 可缩放窗口
    cv2.imshow("Image Display", img)
    cv2.waitKey(0)  # 等待按键关闭窗口
    cv2.destroyAllWindows()
    print(f"成功读取并显示图片：{image_path}，尺寸：{img.shape[0]}x{img.shape[1]}")
else:
    print(f"错误：无法读取图片 {image_path}，请检查路径是否正确！")