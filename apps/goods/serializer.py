# -*- coding:UTF-8 -*-
from django.db.models import Q
from rest_framework import serializers

from apps.goods.models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, HotSearchWords, IndexAd


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ('image',)

class GoodsSerializer(serializers.ModelSerializer):
    #覆盖外键字段
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'

