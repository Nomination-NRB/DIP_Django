import re

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from lib.utils.json_response import success
from .models import Image
from api.serializers import ImageSerializer

from lib.manage.imageProcess import *


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

#class_name url
class resize(APIView):
    def post(self, request):
        # POST参数
        print(request.data)

        function_name= request.data.get('function_name')
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

#url
class getHistArray(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 调用处理函数
        histArray = get_hist_array(path)
        # 返回定制格式的JSON
        return success(histArray)
class reverseChange(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        # 调用处理函数
        dict={}
        dict['filepath']=path
        opera('reverse', dict)
        # 返回定制格式的JSON
        return success(serializer.data)
#class_name->url
class linearChange(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        # dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('gray_three_linear_trans', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class linearChange(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        # dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('gray_three_linear_trans', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class contrast(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('contrast_stretching', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class rotate(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('rotate', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class translate(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('shift_img', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class logChange(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('log', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class reversal(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('flip', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class gammaChange(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('gamma', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class histogramToBalance(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('hist_equal', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class addSaltPepper(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('salt_pepper_noise', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class addGaussian(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('gaussian_noise', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class motion(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('motionBlur', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class wiener(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('wienerFilter', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class selfMedian(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('adaptive_median', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class selfMean(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('adaptive_mean', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)

#class_name->url
class filter(APIView):
    def post(self, request):

        # 获取图片
        images = Image.objects.get(id=request.data.get('id'))
        serializer = ImageSerializer(images, context={'request': request})

        path = re.search(r'media/(.*)', serializer.data['file']).group()
        #以上为复制粘贴操作

        # 调用处理函数
        dict={}
        dict['filepath']=path
        # dict['a']=request.data.get('a')
        # dict['b']=request.data.get('b')
        # dict['c']=request.data.get('c')
        # dict['d']=request.data.get('d')

        opera('median_blur', dict)
        #以下也是复制粘贴
        # 返回定制格式的JSON
        return success(serializer.data)