import os
import time

import cv2
import numpy as np
from video_read import video_read_tqdm
from video_decode import video_decode_known,video_decode_first
from final.qrcode_generate import qr_generate
from video_audio_add import video_audio_add
from watermark_read import watermark_read
from SSIM import compute_ssim,compute_psnr


#video_decode_known('./output/output.mp4',8,0)
#video_decode_first('./output/output.mp4',1)

video_read_tqdm('D:\code from pyCharm\\numpy\opencv\example.mp4','D:\code from pyCharm\\numpy\opencv\\final\output\\test.png','./output/watermarked1.mp4','./output/audio1.mp3',8,0,2)
video_audio_add('./output/watermarked1.mp4', './output/audio1.mp3', f'./output/haveaudio{int(time.time())}.mp4')
os.remove('./output/audio1.mp3')
# # 添加音频必须分着搞，不懂为什么 啊我懂了 啊我不懂
video_decode_known('./output/watermarked1.mp4','.\output\Decoded Watermark.png',8,0)

# PSNR\SSIM
# 读取图像
original_img = cv2.imread("./output/resize watermark.png")
decoded_img = cv2.imread("./output/Decoded Watermark.png")

# 计算 PSNR
psnr_value = compute_psnr(original_img, decoded_img)
print(f"PSNR: {psnr_value:.2f} dB")

# 计算 SSIM
ssim_value = compute_ssim(original_img, decoded_img)
print(f"SSIM: {ssim_value:.4f}")

#img = watermark_read('D:\code from pyCharm\\numpy\opencv\\bird.png')
#cv2.imshow('ing',img*255)
#cv2.waitKey(0)
# 释放资源
cv2.destroyAllWindows()