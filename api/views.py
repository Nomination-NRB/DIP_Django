from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from lib.utils.json_response import success
from lib.utils.json_response import successHttpRequest
from .models import Image
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


class ImageGetAll(APIView):
    def get(self, request):
        print(request.query_params)
        images = Image.objects.get(id=request.query_params.get('id'))
        serializer = ImageSerializer(images)
        return success(serializer.data)
