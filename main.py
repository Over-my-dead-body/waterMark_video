import cv2
import numpy as np
from video_read import video_read_tqdm
from video_decode import video_decode_known
from final.qrcode_generate import qr_generate

video_read_tqdm('D:\code from pyCharm\\numpy\opencv\example.mp4','D:\code from pyCharm\\numpy\opencv\\bird.png','./output/watermarked.mp4',8,4,2)
video_decode_known('./output/output.mp4',8,4)

# 释放资源
cv2.destroyAllWindows()