import json

from django.shortcuts import render
from django.http import HttpResponse
from lib.utils.json_response import success
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    return success('已连接至服务器,可以进行图像处理')


@csrf_exempt
def receive_image(request):
    print(request.data)
    return success('已接收数据')
