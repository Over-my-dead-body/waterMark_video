import cv2
from decode import decode_watermark
from tqdm import tqdm
def video_decode_known(string_video:str,skip_frame:int,Layers:int=0):
    '''
    读取视频并且从指定帧指定层提取水印
    :param string_video: 源视频位置
    :param skip_frame: 隔多少帧一解密
    :param Layers: 解密层数
    :param watermarkWay: 水印生成方式
    :return:
    '''
    # 创建 VideoCapture 对象，读取视频文件
    cap = cv2.VideoCapture(string_video)
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # 获取视频的帧率和尺寸
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 每int(skip_frame)帧插一个水印
    frame_count = 0
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    with tqdm(total=total, desc='Processing') as pbar:
        # 读取视频帧
        while True:
            ret, frame = cap.read()
            # 如果读取到最后一帧，退出循环
            if not ret:
                break

            if frame_count % skip_frame == 0:  # 只有当帧编号是 8 的倍数时才加水印

                # 提取水印
                bo, go, ro = cv2.split(frame)
                decoded_b = decode_watermark(bo, Layers)
                decoded_watermark = cv2.merge([decoded_b, decoded_b, decoded_b])
                cv2.imwrite('.\output\Decoded Watermark.png', decoded_watermark * 255)  # 二值图转0-255显示
            else:
                {}
            pbar.update(1)
            pbar.set_postfix({
                'ETA': f"{pbar.format_interval(pbar.format_dict['elapsed'] / pbar.n * (total - pbar.n))}"
            })
            frame_count += 1

    cap.release()

