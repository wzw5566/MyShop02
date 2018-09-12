# -*- coding:UTF-8 -*-

from .serializer import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.goods.models import Goods


class GoodsListView(APIView):

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serislizer = GoodsSerializer(goods, many=True)
        return Response(goods_serislizer.data)