# -*- coding:UTF-8 -*-

from .serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, mixins, viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.goods.models import  Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from apps.goods.filters import GoodsFilter
from apps.goods.serializer import GoodsSerializer, CategorySerializer, GoodsImageSerializer, BrandSerializer, HotWordsSerializer,BannerSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

class GoodsPagination(PageNumberPagination):
    """
    配置分页
    """
    page_size = 20
    page_size_query_param = "p"
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    """
    获取商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:商品分类列表数据
    """


    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜列表
    """
    queryset = HotSearchWords.objects.all()
    serializer_class = HotWordsSerializer


