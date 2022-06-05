import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_dip_courseproject_django.settings')
django.setup()
# 以上是zeho加的环境变量

import re
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from lib.utils.json_response import success
from lib.manage.imageProcess import *
from api.models import Image
from api.serializers import ImageSerializer


# Create your views here.


class index(APIView):
    def get(self, request):
        return success('已连接至服务器,可以进行图像处理')


class ImageSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, *args, **kwargs):
        print(request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success(serializer.data)

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return success(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success(serializer.data)


# class_name url
class resize(APIView):  # 放大/缩小
    def post(self, request):
        # POST参数
        # print(request.data)
        # X,Y轴变化率
        zoomXValue = request.data.get("zoomXValue")
        zoomYValue = request.data.get("zoomYValue")

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 调用处理函数
        # dict={}
        # dict['filepath']=path
        # dict['Sx']=zoomXValue
        # dict['Sy']=zoomYValue
        # opera('imageResize',dict)
        imageResize(zoomXValue, zoomYValue, path)
        # 返回定制格式的JSON
        return success(serializer.data)


# url
class getHistArray(APIView):
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 调用处理函数
        histArray = get_hist_dict(path)
        # 返回定制格式的JSON
        return success(histArray)


class reverseChange(APIView):  # 反色变换
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        opera('reverse', dict)
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class linearChange(APIView):  # 分段线性变化
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # inputA、inputB、inputC、inputD
        # a、b、c、d
        dict['a'] = int(request.data.get('inputA'))
        dict['b'] = int(request.data.get('inputB'))
        dict['c'] = int(request.data.get('inputC'))
        dict['d'] = int(request.data.get('inputD'))


        opera('gray_three_linear_trans', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class contrast(APIView):  # 对比度拉伸
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('contrast_stretching', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class rotate(APIView):  # 旋转
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # rotateValue
        dict = {}
        dict['filepath'] = path
        dict['angle'] = request.data.get('rotateValue')

        opera('rotate', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class translate(APIView):  # 平移
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # transXValue、transYValue
        # x、y
        dict = {}
        dict['filepath'] = path
        dict['x'] = request.data.get('transXValue')
        dict['y'] = request.data.get('transYValue')

        opera('shift_img', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class logChange(APIView):  # 对数变换
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('log', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class reversal(APIView):  # 翻转
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # spinXVaue、spinYVaue
        # x_flip、y_flip
        dict = {}
        dict['filepath'] = path
        temp = request.data.get('spinXYVaue')
        if temp == 'X':
            dict['x_flip'] = True
            dict['y_flip'] = False
        else:
            dict['x_flip'] = False
            dict['y_flip'] = True
        opera('flip', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class gammaChange(APIView):  # 幂次变换
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # inputGamma
        # gamma
        dict = {}
        dict['filepath'] = path
        dict['gamma'] = eval(request.data.get('inputGamma'))

        opera('gamma', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class histogramToBalance(APIView):  # 直方图均衡化
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('hist_equal', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class histogramToOne(APIView):  # 直方图归一化
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('#zeho', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class addSaltPepper(APIView):  # 椒盐噪声
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # zoomPepperValue、zoomSaltValue
        # pa、pb
        dict = {}
        dict['filepath'] = path
        dict['pa'] = request.data.get('zoomPepperValue')
        dict['pb'] = request.data.get('zoomSaltValue')
        opera('salt_pepper_noise', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class addGaussian(APIView):  # 高斯噪声
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # inputMean、inputVariance
        # mean、var
        dict = {}
        dict['filepath'] = path
        dict['mean'] = float(request.data.get('inputMean'))
        dict['var'] = float(request.data.get('inputVariance'))

        opera('gaussian_noise', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class motion(APIView):  # Motion/Disk模糊操作
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # inputMotionDistance、inputMotionAngle、inputMotionRadius
        # dist、angle、radius
        dict = {}
        dict['filepath'] = path
        if request.data.get('inputMotionDistance') == '':
            dict['dist'] = 0
        else:
            dict['dist'] = float(request.data.get('inputMotionDistance'))
        if request.data.get('inputMotionAngle') == '':
            dict['angle'] = 0
        else:
            dict['angle'] = float(request.data.get('inputMotionAngle'))
        if request.data.get('inputMotionRadius') == '':
            dict['radius'] = 0
        else:
            dict['radius'] = float(request.data.get('inputMotionRadius'))
        opera('motion_disk_Blur', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class wiener(APIView):  # 维纳滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('wienerFilter', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class smooth(APIView):  # 平滑约束复原
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('#zeho', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class selfMedian(APIView):  # 自适应中值滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('adaptive_median', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class selfMean(APIView):  # 自适应均值滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('adaptive_mean', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


# class_name->url
class filter(APIView):  # 平滑滤波（中值/均值）
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        # ValueOfMeanOrMedian、inputMeanOrMedianSize
        # op_name、ksize
        dict = {}
        dict['filepath'] = path
        dict['op_name'] = request.data.get('ValueOfMeanOrMedian')
        temp= int(request.data.get('inputMeanOrMedianSize'))
        if(temp%2==0):
            temp+=1
        dict['ksize'] = temp

        opera('filter', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


class sharpen(APIView):  # 锐化滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('sharpen', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


class fft(APIView):  # 傅里叶变换
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('#zeho', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


class lowFilter(APIView):  # 低通滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('#zeho', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)


class highFilter(APIView):  # 高通滤波
    def post(self, request):
        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 以上为复制粘贴操作

        # 调用处理函数
        dict = {}
        dict['filepath'] = path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('#zeho', dict)
        # 以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)
