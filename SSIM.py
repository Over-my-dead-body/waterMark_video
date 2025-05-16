import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
def compute_ssim(img1, img2, multichannel=True):
    # 确保图像尺寸一致
    assert img1.shape == img2.shape, "图像尺寸不一致"

    # 转换为灰度图（单通道）
    # 如果是彩色图像，设置 multichannel=True（旧版本）或 channel_axis=-1（新版本）
    if len(img1.shape) == 3 and img1.shape[2] == 3:
        ssim_value = ssim(
            img1, img2,
            channel_axis=-1,  # 多通道模式
            data_range=255    # 数据范围（8-bit 图像为 255）
        )
    else:
        ssim_value = ssim(
            img1, img2,
            data_range=255
        )
    return ssim_value

def compute_psnr(img1, img2, max_pixel=255.0):
    """
    计算两张图像的 PSNR 值
    :param img1: 原始图像 (numpy array)
    :param img2: 处理后的图像 (numpy array)
    :param max_pixel: 图像像素最大值，默认为 255
    :return: PSNR 值 (dB)
    """
    assert img1.shape == img2.shape, "图像尺寸不一致"
    assert img1.dtype == img2.dtype, "图像数据类型不一致"

    mse = np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)

    if mse == 0:
        return float("inf")

    psnr = 10 * np.log10(max_pixel ** 2 / mse)
    return psnr


def compute_ssim(img1, img2):
    """
    计算两张图像的 SSIM 值
    :param img1: 原始图像 (numpy array)
    :param img2: 处理后的图像 (numpy array)
    :return: SSIM 值
    """
    assert img1.shape == img2.shape, "图像尺寸不一致"

    # 如果是彩色图，则转换为灰度图
    if len(img1.shape) == 3 and img1.shape[2] == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ssim_value = ssim(img1, img2, data_range=img1.max() - img1.min())
    return ssim_value


# # 示例用法 错误
# img_original = cv2.imread("resize watermark.png")
# img_processed = cv2.imread("./output/Decoded Watermark.png")
# ssim_value = compute_ssim(img_original, img_processed)
# print(f"SSIM: {ssim_value}")



if __name__ == "__main__":
    # 读取图像
    original_img = cv2.imread("./output/resize watermark.png")
    decoded_img = cv2.imread("./output/Decoded Watermark.png")

    # 计算 PSNR
    psnr_value = compute_psnr(original_img, decoded_img)
    print(f"PSNR: {psnr_value:.2f} dB")

    # 计算 SSIM
    ssim_value = compute_ssim(original_img, decoded_img)
    print(f"SSIM: {ssim_value:.4f}")