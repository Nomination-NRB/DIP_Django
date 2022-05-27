from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # 可以处理视图的路由器
router.register('ImageSet', views.ImageSet)  # 向路由器中注册视图集

urlpatterns = [
    path('getHistArray/', views.getHistArray.as_view(), name='getHistArray'),
    path('resize/', views.resize.as_view(), name='resize'),
    path('', views.index.as_view(), name='index'),
]


urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
