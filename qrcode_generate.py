import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer,VerticalBarsDrawer,SquareModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

def qr_generate(data:str,way:int):
    '''
    本函数用于生成二维码
    :param data: 需要加到二维码里的文字，是字符串
    :param way: 生成什么样式的二维码(0-什么都没有最普通二维码，1-竖条二维码，2-横条二维码，3-竖条二维码+下到上渐变)
    :return:
    '''
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    if way == 0:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
    elif way == 1:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
    elif way == 2:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
    elif way == 3:
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer(),
                        color_mask=VerticalGradiantColorMask())


    img.save('./output/test.png')

if __name__ =='__main__':
    data = 'hello world!'
    qr_generate(data,3)