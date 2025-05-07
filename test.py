from watermark_read import watermark_read
import cv2

# watermark_read 测试
img = watermark_read('../duck.png')
cv2.imshow('img',img*255)
cv2.waitKey(0)