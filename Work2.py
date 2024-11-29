import cv2
import numpy as np

# 读取图像
img = cv2.imread('../pic/GGbond.jpg')


# 定义均值滤波函数
def apply_mean_filter(image, ksize):
    # 使用 cv2.blur 函数进行均值滤波
    blurred_img = cv2.blur(image, (ksize, ksize))
    return blurred_img


# 定义不同的窗口大小
ksize_values = [1,3,5,7,9,15,30,60]

# 应用不同窗口大小的均值滤波
for ksize in ksize_values:
    smoothed_img = apply_mean_filter(img, ksize)
      # 显示处理后的图像
    cv2.imshow(f'ksize = {ksize}', smoothed_img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存不同窗口大小处理后的图像
for final_ksize in ksize_values:
    final_smoothed_img = apply_mean_filter(img, final_ksize)
# 保存结果图像
    cv2.imwrite(f'../pic/work2/GGbond_filtered_image{final_ksize}.jpg', final_smoothed_img)
