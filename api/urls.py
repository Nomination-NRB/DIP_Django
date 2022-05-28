from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # 可以处理视图的路由器
router.register('ImageSet', views.ImageSet)  # 向路由器中注册视图集

urlpatterns = [
    path('getHistArray/', views.getHistArray.as_view(), name='getHistArray'),
    path('resize/', views.resize.as_view(), name='resize'),
    path('reverseChange/', views.reverseChange.as_view(), name='reverseChange'),
    path('linearChange/', views.linearChange.as_view(), name='linearChange'),
    path('contrast/', views.contrast.as_view(), name='contrast'),
    path('rotate/', views.rotate.as_view(), name='rotate'),
    path('translate/', views.translate.as_view(), name='translate'),
    path('logChange/', views.logChange.as_view(), name='logChange'),
    path('reversal/', views.reversal.as_view(), name='reversal'),
    path('gammaChange/', views.gammaChange.as_view(), name='gammaChange'),
    path('histogramToBalance/', views.histogramToBalance.as_view(), name='histogramToBalance'),
    path('histogramToOne/', views.histogramToOne.as_view(), name='histogramToOne'),
    path('addSaltPepper/', views.addSaltPepper.as_view(), name='addSaltPepper'),
    path('addGaussian/', views.addGaussian.as_view(), name='addGaussian'),
    path('motion/', views.motion.as_view(), name='motion'),
    path('wiener/', views.wiener.as_view(), name='wiener'),
    path('selfMedian/', views.selfMedian.as_view(), name='selfMedian'),
    path('selfMean/', views.selfMean.as_view(), name='selfMean'),
    path('filter/', views.filter.as_view(), name='filter'),
    path('smooth/', views.smooth.as_view(), name='smooth'),
    path('sharpen/', views.sharpen.as_view(), name='sharpen'),
    path('fft/', views.fft.as_view(), name='fft'),
    path('lowFilter/', views.lowFilter.as_view(), name='lowFilter'),
    path('highFilter/', views.highFilter.as_view(), name='highFilter'),
    path('', views.index.as_view(), name='index'),
]


urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
