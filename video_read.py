import cv2
from tqdm import tqdm
from decode import decode_watermark
from encode import encode_watermark
from resize import resize_photoBORDER_REFLECT,resize_photoBORDER_CONSTANT
from watermark_read import watermark_read

def video_read(string_video:str,string_img:str,string_save:str,skip_frame:int,Layers:int=0,watermarkWay:int=2):
    '''
    读取视频并且将内容添加水印
    :param string_video: 源视频位置
    :param string_img: 水印位置
    :param string_save: 输出文件保存位置
    :param skip_frame: 隔多少帧一加密
    :param Layers: 加密层数
    :param watermarkWay: 水印生成方式
    :return:
    '''
    # 读取水印图像
    watermarkImage = watermark_read(string_img)
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

    # 创建 VideoWriter 对象，保存处理后的视频
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter(string_save, fourcc, fps, (width, height), isColor=True)

    # 每int(skip_frame)帧插一个水印
    frame_count = 0

    # 读取视频帧
    while True:
        ret, frame = cap.read()
        # 如果读取到最后一帧，退出循环
        if not ret:
            break

        if frame_count % skip_frame == 0:  # 只有当帧编号是 8 的倍数时才加水印

            # 帧作为水印载体,提取当前帧的RGB通道（OpenCV默认BGR格式）
            bb, gb, rb = cv2.split(frame)

            # 调整水印尺寸与当前帧匹配
            wat_resized = resize_photoBORDER_CONSTANT(watermarkImage,bb) if watermarkWay == 1 else resize_photoBORDER_REFLECT(
                watermarkImage, bb)

            # 嵌入水印
            encoded_b = encode_watermark(bb, watermarkImage, Layers, watermarkWay)
            encoded_g = encode_watermark(gb, watermarkImage, Layers, watermarkWay)
            encoded_r = encode_watermark(rb, watermarkImage, Layers, watermarkWay)

            # 合并回 BGR 格式
            encoded_frame_bgr = cv2.merge([encoded_b, encoded_g, encoded_r])

            # 写入输出视频
            out.write(encoded_frame_bgr)

            # 提取水印
            bo, go, ro = cv2.split(encoded_frame_bgr)
            decoded_b = decode_watermark(bo, Layers)
            decoded_watermark = cv2.merge([decoded_b, decoded_b, decoded_b])
            cv2.imwrite('.\output\Decoded Watermark.png', decoded_watermark * 255)  # 二值图转0-255显示

            cv2.imwrite('.\output\Frame.png', encoded_frame_bgr)

        else:
            out.write(frame)

        frame_count += 1

    cap.release()
    out.release()

def video_read_tqdm(string_video:str,string_img:str,string_save:str,skip_frame:int,Layers:int=0,watermarkWay:int=2):
    '''
    读取视频并且将内容添加水印,显示进度条
    :param string_video: 源视频位置
    :param string_img: 水印位置
    :param string_save: 输出文件保存位置
    :param skip_frame: 隔多少帧一加密
    :param Layers: 加密层数
    :param watermarkWay: 水印生成方式
    :return:
    '''
    # 读取水印图像
    watermarkImage = watermark_read(string_img)
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

    # 创建 VideoWriter 对象，保存处理后的视频
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter(string_save, fourcc, fps, (width, height), isColor=True)

    # 每int(skip_frame)帧插一个水印
    frame_count = 0

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    with tqdm (total=total,desc='Processing')as pbar:
        # 读取视频帧
        while True:
            ret, frame = cap.read()
            # 如果读取到最后一帧，退出循环
            if not ret:
                break

            if frame_count % skip_frame == 0:  # 只有当帧编号是 8 的倍数时才加水印

                # 帧作为水印载体,提取当前帧的RGB通道（OpenCV默认BGR格式）
                bb, gb, rb = cv2.split(frame)

                # 调整水印尺寸与当前帧匹配
                wat_resized = resize_photoBORDER_CONSTANT(watermarkImage,
                                                          bb) if watermarkWay == 1 else resize_photoBORDER_REFLECT(
                    watermarkImage, bb)

                # 嵌入水印
                encoded_b = encode_watermark(bb, watermarkImage, Layers, watermarkWay)
                encoded_g = encode_watermark(gb, watermarkImage, Layers, watermarkWay)
                encoded_r = encode_watermark(rb, watermarkImage, Layers, watermarkWay)

                # 合并回 BGR 格式
                encoded_frame_bgr = cv2.merge([encoded_b, encoded_g, encoded_r])

                # 写入输出视频
                out.write(encoded_frame_bgr)

                # 提取水印
                bo, go, ro = cv2.split(encoded_frame_bgr)
                decoded_b = decode_watermark(bo, Layers)
                decoded_watermark = cv2.merge([decoded_b, decoded_b, decoded_b])
                cv2.imwrite('.\output\Decoded Watermark.png', decoded_watermark * 255)  # 二值图转0-255显示

                cv2.imwrite('.\output\Frame.png', encoded_frame_bgr)

            else:
                out.write(frame)

            pbar.update(1)
            pbar.set_postfix({
                'ETA': f"{pbar.format_interval(pbar.format_dict['elapsed'] / pbar.n * (total - pbar.n))}"
            })
            frame_count += 1

    cap.release()
    out.release()