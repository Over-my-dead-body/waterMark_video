import cv2

def watermark_read(string:str):
    '''
    本函数用于读取并二值化水印图像
    :param string: 图像位置
    :return: 读取后并二值化了的图像
    '''
    watermarkImage = cv2.imread(string, cv2.IMREAD_GRAYSCALE)
    _, watermarkImage = cv2.threshold(watermarkImage, 127, 1, cv2.THRESH_BINARY)
    return watermarkImage