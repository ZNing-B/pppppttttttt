import cv2
import numpy as np

# 读取彩色图像
img = cv2.imread('../pic/GGbond.jpg')

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 伽马变换函数
def gamma_correction(image, gamma):
    # 归一化到 0-1 之间
    normalized_img = image / 255.0
    # 应用伽马变换
    corrected_img = np.power(normalized_img, gamma)
    # 重新缩放到 0-255
    corrected_img = np.uint8(corrected_img * 255)
    return corrected_img

# 设置伽马值并应用伽马变换
gamma_value = 1   # 可以根据需要调整
adjusted_gray = gamma_correction(gray_img, gamma_value)

# 显示结果
cv2.imshow('Gamma Adjusted Gray Image', adjusted_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存调整后的图像
cv2.imwrite(f'../pic/gray_image_gamma_{gamma_value}.jpg', adjusted_gray)
