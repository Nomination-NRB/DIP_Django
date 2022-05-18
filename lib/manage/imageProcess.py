import cv2

from urllib import parse

from python_dip_courseproject_django.settings import MEDIA_ROOT


def imageResize(x, y, filePath):
    filePath = parse.unquote(filePath)
    img = cv2.imread(filePath)
    x = float(x)
    y = float(y)
    out = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(filePath, out)


def get_hist_array(file_path):
    """
    直方图数组获取

    参数:
        filePath: 图片路径
    返回:
        histArray: 直方图数组
        灰度直方返回值: [0, 256]
        RGB直方返回值: [[0, 256], [0, 256], [0, 256]]
    """
    filepath = parse.unquote(file_path)
    img = cv2.imread(filepath)
    img0 = img[:, :, 0]
    img1 = img[:, :, 1]
    img2 = img[:, :, 2]
    if (img0 == img1 == img2).all():
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    else:
        hist = [cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1),
                cv2.calcHist([img], [1], None, [256], [0, 256]).reshape(-1),
                cv2.calcHist([img], [2], None, [256], [0, 256]).reshape(-1)]

    return hist
