import cv2

def resize_photoBORDER_REFLECT(initImage,targetImage):
    '''
    反射-重新设置图片大小
    :param initImage: 原图片
    :param targetImage: 目标大小图片
    :return: 大小与目标一致的反射形成的图片
    '''
    # 获取目标图像的尺寸（假设targetImage是载体图像的一个通道，shape为 (h, w)）
    target_h, target_w = targetImage.shape[:2]
    # 获取初始图像的尺寸
    init_h, init_w = initImage.shape[:2]
    # 计算需要填充的高度和宽度
    pad_h = max(target_h - init_h, 0)
    pad_w = max(target_w - init_w, 0)
    # 使用反射填充（若目标尺寸更大则填充，否则裁剪）
    resized = cv2.copyMakeBorder(
        initImage,
        top=0,
        bottom=pad_h,
        left=0,
        right=pad_w,
        borderType=cv2.BORDER_REFLECT
    )
    # 确保最终尺寸与目标一致（若目标更小则裁剪）
    resized = resized[:target_h, :target_w]
    return resized
def resize_photoBORDER_CONSTANT(initImage,targetImage):
    '''
    直接-重新设置图片大小
    :param initImage: 原图片
    :param targetImage: 目标大小图片
    :return: 大小与目标一致的直接形成的图片
    '''
    # 获取目标图像的尺寸（假设targetImage是载体图像的一个通道，shape为 (h, w)）
    target_h, target_w = targetImage.shape[:2]
    # 获取初始图像的尺寸
    init_h, init_w = initImage.shape[:2]
    # 计算需要填充的高度和宽度
    pad_h = max(target_h - init_h, 0)
    pad_w = max(target_w - init_w, 0)
    # 使用反射填充（若目标尺寸更大则填充，否则裁剪）
    resized = cv2.copyMakeBorder(
        initImage,
        top=0,
        bottom=pad_h,
        left=0,
        right=pad_w,
        borderType=cv2.BORDER_CONSTANT,
        value=0
    )
    # 确保最终尺寸与目标一致（若目标更小则裁剪）
    resized = resized[:target_h, :target_w]
    return resized
def resize_photo(initImage, targetImage, border_type=cv2.BORDER_REFLECT, value=0):
    """
    图片重新设置大小，可选择 单独与反射 两种方式
    :param initImage: 原图片
    :param targetImage: 目标大小图片
    :param border_type: 设置大小方式
    :param value:
    :return:
    """
    target_h, target_w = targetImage.shape[:2]
    init_h, init_w = initImage.shape[:2]
    pad_h = max(target_h - init_h, 0)
    pad_w = max(target_w - init_w, 0)
    resized = cv2.copyMakeBorder(
        initImage, 0, pad_h, 0, pad_w,
        borderType=border_type,
        value=value
    )
    return resized[:target_h, :target_w]