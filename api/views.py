import json

from django.shortcuts import render
from django.http import HttpResponse

from api.serializers import ImageSerializer
from lib.utils.json_response import success

from rest_framework.viewsets import ModelViewSet
from .models import Image

# Create your views here.


def index(request):
    return success('已连接至服务器,可以进行图像处理')


class receive_image(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer