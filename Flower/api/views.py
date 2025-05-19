import random
import time

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from utils import return_code
from utils.filters import FlowerFilterSet, UserFilterSet, OrderFilterSet, AnnouncementFilterSet, SelfFilterBackend
from utils.jwt_auth import create_token
from . import models
from .serializers import LoingSerializer, RegisterSerializer, FlowerSerializer, UserSerializer, AnnouncementSerializer, \
    BannerSerializer, OrderSerializer


class LoginView(APIView):
    """ 用户登录 """
    authentication_classes = []

    # 2. 数据库校验用户名和密码的合法性
    def post(self, request):
        # 1. 获取用户请求 & 校验
        serializer = LoingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"code": return_code.VALIDATE_ERROR, 'detail': serializer.errors})

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user_object = models.UserInfo.objects.filter(username=username, password=password).first()

        if not user_object:
            return Response({"code": return_code.VALIDATE_ERROR, "error": "用户名或密码错误"})

        # 用户名密码正确生成token
        token = create_token({"user_id": user_object.id, "username": user_object.username})
        return Response({'code': return_code.SUCCESS, 'token': token,
                         'username': user_object.username, 'role': user_object.role})


class RegisterView(CreateModelMixin, GenericViewSet):
    """ 用户注册 """
    authentication_classes = []
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.validated_data.pop('confirm_password')
        serializer.save()


class FlowerView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    """ 鲜花功能：需认证 """
    queryset = models.Flower.objects.all().order_by('-create_time', '-id')
    serializer_class = FlowerSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = FlowerFilterSet


class UserView(ListModelMixin, DestroyModelMixin, GenericViewSet):
    """ 用户管理 """
    queryset = models.UserInfo.objects.all().order_by('-create_time')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = UserFilterSet


class AnnouncementView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    """ 公告管理 """
    queryset = models.Announcement.objects.all().order_by('-create_time')
    serializer_class = AnnouncementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AnnouncementFilterSet

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user['user_id'])


class BannerView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    """ 轮播图管理 """
    queryset = models.Banner.objects.all().order_by('-create_time')
    serializer_class = BannerSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user['user_id'])


class OrderView(ListModelMixin, CreateModelMixin, DestroyModelMixin,GenericViewSet):
    """ 订单管理 """
    queryset = models.Order.objects.all().order_by('-create_time', '-id')
    serializer_class = OrderSerializer
    filter_backends = [SelfFilterBackend, DjangoFilterBackend, ]
    filterset_class = OrderFilterSet

    def perform_create(self, serializer):
        user = self.request.user['user_id']
        flower_id = serializer.validated_data['flower'].id  # 鲜花id
        quantity = serializer.validated_data['quantity']  # 购买鲜花总数量
        flower_object = models.Flower.objects.filter(id=flower_id).first()

        if not flower_object:
            return Response({'code': 3000, 'msg': '该鲜花不存在'})

        # 购买数量大于库存量则不可以继续购买
        if quantity > flower_object.stock:
            return Response({'code': 3002, 'msg': f'库存量还剩{flower_object.stock}'})

        if flower_object.stock <= 0:
            return Response({'code': 3003, 'msg': '该品种已售馨'})
        order_num = f"{time.strftime('%Y%m%d%H%M%S')}{random.randint(10000000, 99999999)}"
        order_object = models.Order.objects.create(flower_id=flower_id, quantity=quantity,
                                                   total_price=quantity * flower_object.price, user_id=user,
                                                   order_num=order_num)

        flower_object.stock -= quantity
        flower_object.save()

        return Response({"code": return_code.SUCCESS, 'data': {'active': True}})
