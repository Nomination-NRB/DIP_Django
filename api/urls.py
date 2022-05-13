from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()  # 可以处理视图的路由器
router.register('uploadImage', views.receive_image)  # 向路由器中注册视图集
print(router.urls)

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中