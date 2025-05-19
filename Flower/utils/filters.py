from django_filters import FilterSet, filters
from rest_framework.filters import BaseFilterBackend

from api import models


# 编写搜索条件类

class FlowerFilterSet(FilterSet):
    """ 鲜花搜索 """
    name = filters.CharFilter(field_name="name", lookup_expr="contains")

    class Meta:
        model = models.Flower
        fields = ['name']


class UserFilterSet(FilterSet):
    """ 用户搜索 """
    username = filters.CharFilter(field_name="username", lookup_expr="contains")
    name = filters.CharFilter(field_name="name", lookup_expr="contains")

    class Meta:
        model = models.UserInfo
        fields = ['username', 'name']


class OrderFilterSet(FilterSet):
    """ 订单搜索：根据订单号搜索 """
    order_num = filters.CharFilter(field_name="order_num", lookup_expr="contains")

    class Meta:
        model = models.Order
        fields = ['order_num']


class AnnouncementFilterSet(FilterSet):
    """ 公告搜索：根据标题搜索 """
    title = filters.CharFilter(field_name="title", lookup_expr="contains")

    class Meta:
        model = models.Announcement
        fields = ['title']


class SelfFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user['username'] == 'admin':
            return queryset.filter()
        else:
            return queryset.filter(user=request.user['user_id'])
