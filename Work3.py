import cv2
import numpy as np

# 读取彩色图像
img = cv2.imread('../pic/flower.jpg')

# 定义K1的Sobel滤波核
k1_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # Gx
k1_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # Gy

# 定义K2的差分模板滤波核
k2_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  # G'x
k2_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])  # G'y


# 对彩色图像的每个通道进行滤波处理
def apply_filter_to_color(image, kernel_x, kernel_y):
    channels = cv2.split(image)  # 分离彩色图像的通道
    processed_channels = []

    for channel in channels:
        grad_x = cv2.filter2D(channel, cv2.CV_64F, kernel_x)
        grad_y = cv2.filter2D(channel, cv2.CV_64F, kernel_y)
        result = np.abs(grad_x) + np.abs(grad_y)
        result = cv2.convertScaleAbs(result)  # 转换为 uint8
        processed_channels.append(result)

    # 合并处理后的通道
    return cv2.merge(processed_channels)


# 使用 K1 进行滤波
K1_result = apply_filter_to_color(img,k1_x, k1_y)

# 使用 K2 进行滤波
K2_result = apply_filter_to_color(img, k2_x, k2_y)

# 显示结果
cv2.imshow('Original Image', img)
cv2.imshow('K1  Filtered Image', K1_result)
cv2.imshow('K2  Filtered Image', K2_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果图像
cv2.imwrite('../pic/work3/K1_Image.jpg', K1_result)
cv2.imwrite('../pic/work3/K2_Image.jpg', K2_result)
