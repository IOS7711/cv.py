# 引入OpenCV库（Python中OpenCV的包名是cv2），用于后续的图像/视频处理
import cv2

# 调用cv2.getVersionString()获取当前安装的OpenCV版本号，并打印输出
print(cv2.getVersionString())

# 用cv2.imread()读取当前目录下的"try.jpg"图片
# 读取成功则返回存储像素数据的NumPy数组，失败则返回None
image = cv2.imread("try.jpg")

# 校验图片是否读取成功
if image is not None:
    # shape是NumPy数组的属性，输出格式为(高度, 宽度, 通道数)
    # 例如(480, 640, 3)表示高480像素、宽640像素、3个颜色通道
    print(image.shape)

    # 创建名为"Image"的窗口，并在窗口中显示读取到的图片
    cv2.imshow("Image", image)

    # 暂停程序，无限等待键盘输入（按下任意键后继续执行）
    # 若不写这行，imshow的窗口会立即关闭
    cv2.waitKey(0)

    # 关闭所有由OpenCV创建的窗口，释放资源
    cv2.destroyAllWindows()
else:
    # 若image为None，说明图片读取失败，打印错误提示
    print("错误：图片读取失败，请检查路径或文件是否存在！")
