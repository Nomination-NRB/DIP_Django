import cv2
from python_dip_courseproject_django.settings import MEDIA_ROOT


def imageResize(x, y, filePath):
    print(filePath)
    img = cv2.imread(filePath)
    x=float(x)
    y=float(y)
    out = cv2.resize(img,None, fx=x, fy=y,interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(filePath, out)