"""MyShop02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from MyShop02.settings import MEDIA_ROOT
from django.views.static import serve

from extra_apps import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, CategoryViewSet

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from MyShop02.settings import MEDIA_ROOT
from django.views.static import serve
#from apps.users.views import SmsCodeViewset, UserViewset

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'categorys', CategoryViewSet, base_name="categorys")



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    #     jwt的认证接口
    url(r'^login', obtain_jwt_token),


]
