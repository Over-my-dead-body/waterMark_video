import cv2
from resize import resize_photo

def encode_watermark(bed, wat, Layers, way):
    '''
    本函数用于对彩色图像进行二值化水印加密
    :param bed: 需要加密的彩色图像
    :param wat: 二值化水印图像
    :param Layers: 水印加密层数
    :param way: 水印加密方式（1-单水印/ 2-反射水印）
    :return: 返回加密水印后的图像
    '''
    if way == 1:
        wat = resize_photo(wat, bed, cv2.BORDER_CONSTANT, 0)
    elif way == 2:
        wat = resize_photo(wat, bed, cv2.BORDER_REFLECT)
    else:
        raise ValueError("way参数必须为1或2")
    bed = bed.copy()
    height, width = bed.shape[:2]
    for i in range(height):
        for j in range(width):
            w = bed[i][j] // (2 ** Layers)
            if w % 2 == 0 and wat[i][j] == 1:
                new_val = bed[i][j] + (2 ** Layers)
                bed[i][j] = min(new_val, 255)
            elif w % 2 == 1 and wat[i][j] == 0:
                new_val = bed[i][j] - (2 ** Layers)
                bed[i][j] = max(new_val, 0)
    return bed