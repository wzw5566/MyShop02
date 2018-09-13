# -*- coding:UTF-8 -*-

from .serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, mixins, viewsets


from apps.goods.models import Goods
from apps.goods.serializer import GoodsSerializer, CategorySerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

class GoodsPagination(PageNumberPagination):
    """
    配置分页
    """
    page_size = 20
    page_size_query_param = "p"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    """
    list all goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination



"""
#精简前代码
class GoodsListView(APIView):

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serislizer = GoodsSerializer(goods, many=True)
        return Response(goods_serislizer.data)
"""