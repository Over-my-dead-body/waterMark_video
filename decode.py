import cv2
import numpy as np

def decode_watermark(bed, Layers):
    '''
    本函数用于从图片中解密水印
    :param bed: 加密后的图片
    :param Layers: 水印所在层数
    :return: 解密出的水印二值图片
    '''
    height, width = bed.shape[:2]
    wat = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            w = bed[i][j] // (2 ** Layers)
            wat[i][j] = 1 if (w % 2 == 1) else 0
    return wat