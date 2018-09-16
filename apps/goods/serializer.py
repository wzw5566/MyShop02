# -*- coding:UTF-8 -*-
from django.db.models import Q
from rest_framework import serializers

from apps.goods.models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords, IndexAd

class CategorySerializer3(serializers.ModelSerializer):
    """
    三级分类
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    """
    一级分类
    """
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsImageSerializer(serializers.ModelSerializer):
    """
    产品图片
    """
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

class HotWordsSerializer(serializers.ModelSerializer):
    """
    热搜词
    """

    class Meta:
        model = HotSearchWords
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    """
    轮播banner
    """
    class Meta:
        model = Banner
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """
    品牌
    """
    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'