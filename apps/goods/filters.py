
# -*- coding:UTF-8 -*-
from apps.goods.models import Goods
import django_filters
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """商品过滤器"""
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    #商品的模糊搜索，其中'contains'代表区分大小写，'icontains'代表不区分大小写
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter()
    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name', 'is_hot', 'is_new']

