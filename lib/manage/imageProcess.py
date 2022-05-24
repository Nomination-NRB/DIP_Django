import cv2

from urllib import parse

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

def opera(op,dict):
    '''
    参数:
        op: 操作函数名 string op='zoom'
        dict: 参数字典:dict {'Sx':1.5,'Sy':1.5,'filePath':'xxx.jpg'}
        其中dict['filePath']为图片路径
    '''
    dict['filePath'] = parse.unquote(dict['filePath'])
    paradict=dict.copy()
    del paradict['filePath']
    img = cv2.imread(dict['filePath'])
    imgType = judge_img_type(img)
    if imgType == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out=eval(op)(img,**paradict)
    cv2.imwrite(dict['filePath'], out)

def imageResize(x, y, filePath):
    filePath = parse.unquote(filePath)
    img = cv2.imread(filePath)
    x = float(x)
    y = float(y)
    out = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(filePath, out)


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
    # cv2是显示bgr的
    hist_dict={'r':[],'g':[],'b':[],'gray':[]}
    if imgType == 'gray':
        hist_dict['gray'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
    else:
        hist_dict['b'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
        hist_dict['g'] = cv2.calcHist([img], [1], None, [256], [0, 256]).reshape(-1)
        hist_dict['r'] = cv2.calcHist([img], [2], None, [256], [0, 256]).reshape(-1)
    return hist_dict