import cv2
import numpy as np

# 读取图像
img = cv2.imread('../pic/GGbond.jpg')
# 转换为 YUV 色彩空间
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# 提取亮度通道 (Y 通道)
y_channel = yuv_img[:, :, 0]


def gamma_correction(image, gamma):
    # 归一化到 0-1 之间
    normalized_img = image / 255.0
    # 应用伽马变换
    corrected_img = np.power(normalized_img, gamma)
    # 重新缩放到 0-255
    corrected_img = np.uint8(corrected_img * 255)
    return corrected_img

# 设置伽马值并应用伽马变换 (调整对比度)

gamma_value = 0.1  # 可以调整此值,以1为界限，越大新图片越暗，越小新图片越亮

adjusted_y = gamma_correction(y_channel, gamma_value)

# 将调整后的 Y 通道赋回
yuv_img[:, :, 0] = adjusted_y

# 转换回 BGR 色彩空间
adjusted_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)

# 显示结果
cv2.imshow('Adjusted Image', adjusted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存调整后的图像
cv2.imwrite('../pic/work1/gamma_0.1.jpg', adjusted_img)
