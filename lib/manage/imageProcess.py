import cv2

from urllib import parse


def imageResize(x, y, filePath):
    filePath = parse.unquote(filePath)
    img = cv2.imread(filePath)
    x = float(x)
    y = float(y)
    out = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_LINEAR)

def judge_img_type(img):
    """
    判断图片类型

    参数:
        img: 图片
    返回:
        imgType: 图片类型:rgb/gray string
    """
    img0 = img[:, :, 0]
    img1 = img[:, :, 1]
    img2 = img[:, :, 2]
    if (img0 == img1).all() and (img0 == img2).all():
        imgType = 'gray'
    else:
        imgType = 'rgb'
    return imgType

def get_hist_dict(filePath):
    """
    获取图片直方图

    参数:
        filepath: 图片路径
    返回:
        hist_dict: 图片直方图:dict
    """
    filepath = parse.unquote(filePath)
    img = cv2.imread(filepath)
    imgType = judge_img_type(img)
    if imgType == 'gray':
        hist_dict['gray'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
    else:
        hist_dict['r'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
        hist_dict['g'] = cv2.calcHist([img], [1], None, [256], [0, 256]).reshape(-1)
        hist_dict['b'] = cv2.calcHist([img], [2], None, [256], [0, 256]).reshape(-1)
    return hist_dict