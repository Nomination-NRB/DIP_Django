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
        dict: 参数字典:dict {'Sx':1.5,'Sy':1.5,'filepath':'xxx.jpg'}
        其中dict['filepath']为图片路径
    '''
    dict['filepath'] = parse.unquote(dict['filepath'])
    paradict=dict.copy()
    del(paradict['filepath'])
    img = cv2.imread(dict['filepath'])
    imgType = judge_img_type(img)
    if imgType == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out=eval(op)(img,**paradict)
    cv2.imwrite(dict['filepath'], out)

def imageResize(Sx, Sy, filePath):
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

# 数图的原函数

#灰度基本变换
# 图像反转
def reverse(img):
    return 255-img

# 对数变换
def log(img,c=1):
    '''
    对数变换

    参数:
        img: 图片
        c: 参数 常数
    '''
    return c*np.log(1.0+img)

# 伽马变换 幂次变换
def gamma(img, gamma=2., eps=0.):
    return 255.*((img+eps)/255.)**gamma

def hist_equal(img):
    return cv2.equalizeHist(img)

# 分段线性变换
def gray_three_linear_trans(input, a, b, c=0, d=255):
    '''
    把[a,b]灰度拓展到[c,d]
    '''
    if a == b or b == 255:
        return None
    #得到掩码
    m1 = (input < a)
    m2 = (a <= input) & (input <= b)
    m3 = (input > b)

    out = (c/a*input)*m1\
        + ((d-c)/(b-a)*(input-a)+c)*m2\
        + ((255-d)/(255-b)*(input-b)+d)*m3
    return out

def contrast_stretching(img, m=255., eps=0., E=2.):
    return 1./(1+(m/(img+eps))**E)

#噪声
# 椒盐噪声
def salt_pepper_noise(img,prob=0.1):
    '''
    prob:椒盐噪声比例
    '''
    H,W=img.shape
    out=img.copy()
    # 椒盐噪声
    for y in range(H):
        for x in range(W):
            rdn=np.random.randint(0,100)
            if rdn<prob:
                out[y,x]=0
            elif rdn>100-prob:
                out[y,x]=255
    return


# 高斯噪声
def gaussian_noise(img,mean=0,var=4):
    '''
    mean:均值
    var:方差
    '''
    H,W=img.shape
    out=img.copy()
    # 高斯噪声
    for y in range(H):
        for x in range(W):
            rdn=np.random.randn(1)
            out[y,x]=out[y,x]+rdn*var+mean
    return out

# 均匀噪声
def mean_noise(img,mean=10,var=100):
    a=2*mean-np.sqrt(12*var)
    b=2*mean+np.sqrt(12*var)
    img_noise=np.random.uniform(a,b,img.shape)
    out=img+img_noise
    out_normal=np.uint8(cv2.normalize(out,None,0,255,cv2.NORM_MINMAX))
    return out_normal




#平滑锐化滤波
# 高斯滤波

# 均值滤波
def mean_blur(img,ksize):
    '''
    ksize 滤波核大小
    '''
    return cv2.blur(img,(ksize,ksize))

def median_blur(img,ksize):
    return cv2.medianBlur(img,ksize)

# 自适应局部降噪
def adaptive_mean(img,m=5,n=None):
    '''
    m*n:均值降噪窗口大小
    '''
    eps=1e-8
    if n==None:
        n=m
    imgAda=np.zeros(img.shape)
    hPad=int((m-1)/2)
    wPad=int((n-1)/2)
    imgPad=np.pad(img.copy(),((hPad,m-hPad-1),(wPad,n-wPad-1)),'edge')
    _,std=cv2.meanStdDev(img)
    var=std**2
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pad=imgPad[i:i+m,j:j+n]
            gxy=img[i,j]
            zSxy=np.mean(pad)
            varSxy=np.var(pad)
            rateVar=min(var/(varSxy+eps),1.0)
            imgAda[i,j]=gxy-rateVar*(gxy-zSxy)
    return imgAda

# 自适应中值
def adaptive_median(img,smax=7):
    m,n=smax,smax
    hPad=int((m-1)/2)
    wPad=int((n-1)/2)
    imgPad=np.pad(img.copy(),((hPad,m-hPad-1),(wPad,n-wPad-1)),'edge')
    imgAda=np.zeros(img.shape)
    for i in range(hPad,img.shape[0]+hPad):
        for j in range(wPad,img.shape[1]+wPad):
            ksize=3
            k=int(ksize/2)
            pad=imgPad[i-k:i+k+1,j-k:j+k+1]
            zxy=img[i-hPad,j-wPad]
            zmin=np.min(pad)
            zmax=np.max(pad)
            zmed=np.median(pad)

            if zmin<zmed<zmax:
                if zmin<zxy<zmax:
                    imgAda[i-hPad,j-wPad]=zxy
                else:
                    imgAda[i-hPad,j-wPad]=zmed
            else:
                while True:
                    ksize+=2
                    k=int(ksize/2)
                    if zmin<zmed<zmax or ksize>smax:
                        break
                    pad=imgPad[i-k:i+k+1,j-k:j+k+1]
                    zmed=np.median(pad)
                    zmin=np.min(pad)
                    zmax=np.max(pad)
                if zmin<zmed<zmax or ksize>smax:
                    if zmin<zxy<zmax:
                        imgAda[i-hPad,j-wPad]=zxy
                    else:
                        imgAda[i-hPad,j-wPad]=zmed
    return imgAda

# 锐化滤波
# sobel
def sobel(img,ksize=3):
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=ksize)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=ksize)
    abs_sobelx = cv2.convertScaleAbs(sobelx)
    abs_sobely = cv2.convertScaleAbs(sobely)
    sobel = np.uint8(cv2.normalize(abs(sobelx)+abs(sobely),None,0,255,cv2.NORM_MINMAX))
    # return abs_sobelx,abs_sobely,sobel
    return sobel

def laplacian(img,ksize=1):
    return cv2.Laplacian(img,cv2.CV_64F,ksize=ksize)

def prewitt(img):
    prewitt_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    prewitt_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    prewitt_x_img=cv2.convertScaleAbs(cv2.filter2D(img,cv2.CV_64F,prewitt_x))
    prewitt_y_img=cv2.convertScaleAbs(cv2.filter2D(img,cv2.CV_64F,prewitt_y))
    imgPrewitt = np.uint8(cv2.normalize(
        abs(prewitt_x_img) + abs(prewitt_y_img), None, 0, 255, cv2.NORM_MINMAX))
    # return prewitt_x_img,prewitt_y_img,imgPrewitt
    return imgPrewitt

def roberts(img):
    kernel_Roberts_x = np.array([[1, 0], [0, -1]])
    kernel_Roberts_y = np.array([[0, -1], [1, 0]])
    imgRoberts_x = cv2.filter2D(img, -1, kernel_Roberts_x)
    imgRoberts_y = cv2.filter2D(img, -1, kernel_Roberts_y)
    imgRoberts = np.uint8(cv2.normalize(
        abs(imgRoberts_x) + abs(imgRoberts_y), None, 0, 255, cv2.NORM_MINMAX))
    # return imgRoberts_x,imgRoberts_y,imgRoberts
    return imgRoberts

def LoG(img,ksize=3):
    out=cv2.GaussianBlur(img,(ksize,ksize),0)
    out=cv2.convertScaleAbs(cv2.Laplacian(out,cv2.CV_64F,ksize))
    return out
# 高斯滤波
def gaussian(img,ksize=3,sigma=0):
    if sigma==0:
        sigma=ksize/2
    return cv2.GaussianBlur(img,(ksize,ksize),sigma)

#基本图像操作
def shift_img(img, x, y):
    '''
    图像平移

    参数:
        img:图像
        x:x轴平移量
        y:y轴平移量
    返回值:
        平移后的图像
    '''
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted

def rotate(img, angle, x_center=0.5, y_center=0.5, scale=1):
    '''
    图像旋转

    参数:
        img:图像
        angle:旋转角度
        x_center:x轴中心比例
        y_center:y轴中心比例
        scale:缩放比例
    返回值:
        旋转后的图像
    '''
    h, w = img.shape[:2]
    center = (x_center * w, y_center * h)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated

#基本灰度变换
# 对数变换
def log(img,c=1):
    return c*np.log(1.0+img)
def flip(image,x_flip=False,y_flip=False):
    '''
    图像翻转

    参数:
        image:图像
        x_flip:x轴翻转
        y_flip:y轴翻转
    返回值:
        翻转后的图像
    '''
    if x_flip:
        image=cv2.flip(image,0)
    if y_flip:
        image=cv2.flip(image,1)
    return image

# 图像复原
def motionBlur(image,angle, dist,eps=1e-6):
    shape=image.shape
    xCenter = (shape[0] - 1) / 2
    yCenter = (shape[1] - 1) / 2
    sinVal = np.sin(angle * np.pi / 180)
    cosVal = np.cos(angle * np.pi / 180)
    PSF = np.zeros(shape)
    for i in range(dist):
        xOffset = round(sinVal * i)
        yOffset = round(cosVal * i)
        PSF[int(xCenter - xOffset), int(yCenter + yOffset)] = 1
    PSF= PSF / PSF.sum()
    fftImg = np.fft.fft2(image)  # 进行二维数组的傅里叶变换
    fftPSF = np.fft.fft2(PSF) + eps
    fftBlur = np.fft.ifft2(fftImg * fftPSF)
    fftBlur = np.abs(np.fft.fftshift(fftBlur))
    return fftBlur

def wienerFilter(img,PSF=None,eps=0,K=0):
    fftImg = np.fft.fft2(img)
    if PSF.all==None:
        return np.abs(np.fft.ifft2(fftImg-K))
    else:
        fftPSF = np.fft.fft2(PSF) + eps
    fftWiener = np.conj(fftPSF) / (np.abs(fftPSF)**2 + K)
    imgWienerFilter = np.fft.ifft2(fftImg * fftWiener)
    imgWienerFilter = np.abs(np.fft.fftshift(imgWienerFilter))
    return imgWienerFilter