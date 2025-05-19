import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api import models


class LoingSerializer(serializers.Serializer):
    """ 用户登录 """
    username = serializers.CharField(label="用户名", write_only=True, required=False)  # 不提交
    password = serializers.CharField(label="密码", min_length=6, write_only=True)

    def validate_username(self, value):
        username = self.initial_data.get("username")
        if not username:
            raise ValidationError("用户名不能为空")
        return value


class RegisterSerializer(serializers.ModelSerializer):
    """ 用户注册 """
    confirm_password = serializers.CharField(label="确认密码", min_length=6, max_length=16, write_only=True)
    password = serializers.CharField(label="密码", min_length=6, max_length=16, write_only=True)
    sex_text = serializers.CharField(label='性别', read_only=True)

    class Meta:
        model = models.UserInfo
        fields = ['username', "password", "confirm_password", 'name', 'sex', 'sex_text', 'phone', 'addr']

    def validate_username(self, value):
        exists = models.UserInfo.objects.filter(username=value).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return value

    def validate_phone(self, value):
        exists = models.UserInfo.objects.filter(phone=value).exists()
        if exists:
            raise ValidationError("手机号已存在")
        if not re.match(r'^1[3-9]\d{9}', value):
            raise ValidationError("手机号格式错误")
        return value

    def validate_confirm_password(self, value):
        password = self.initial_data.get('password')
        if password == value:
            return value
        raise ValidationError("两次密码不一致")


class FlowerSerializer(serializers.ModelSerializer):
    """ 鲜花序列化器 """
    create_time = serializers.DateTimeField(label='鲜花新增时间', format='%Y-%m-%d %X', read_only=True)

    class Meta:
        model = models.Flower
        fields = ['id', 'name', 'stock', 'price', 'image', 'flower_language', 'create_time']


class UserSerializer(serializers.ModelSerializer):
    """ 用户管理序列化器 """
    role_text = serializers.CharField(label='角色', source='get_role_display', read_only=True)
    sex_text = serializers.CharField(label='性别', source='get_sex_display', read_only=True)
    create_time = serializers.DateTimeField(label='用户新增时间', format='%Y-%m-%d %X', read_only=True)

    class Meta:
        model = models.UserInfo
        fields = ['id','role_text', 'username', 'name', 'sex_text', 'avatar', 'phone', 'addr', 'create_time']


class AnnouncementSerializer(serializers.ModelSerializer):
    """ 公告序列化器 """
    create_time = serializers.DateTimeField(label='公告新增时间', format='%Y-%m-%d %X', read_only=True)
    username = serializers.CharField(label='用户', source='user.username', read_only=True)

    class Meta:
        model = models.Announcement
        fields = ['id','create_time', 'title', 'content', 'username']


class BannerSerializer(serializers.ModelSerializer):
    """ 轮播图序列化器 """
    create_time = serializers.DateTimeField(label='轮播图新增时间', format='%Y-%m-%d %X', read_only=True)
    username = serializers.CharField(label='用户', source='user.username', read_only=True)
    image = serializers.CharField(required=True)

    class Meta:
        model = models.Banner
        fields = ['id','create_time', 'image', 'username']


class OrderSerializer(serializers.ModelSerializer):
    """ 订单序列化器 """
    create_time = serializers.DateTimeField(label='下单时间', format='%Y-%m-%d %X', read_only=True)
    order_status_text = serializers.CharField(label='订单状态', source='get_order_status_display', read_only=True)
    flower_text = serializers.CharField(label='鲜花', source='flower.name', read_only=True)
    flower_img = serializers.CharField(label='鲜花', source='flower.image', read_only=True)
    username = serializers.CharField(label='用户', source='user.username', read_only=True)

    class Meta:
        model = models.Order
        fields = ['id','user', 'create_time', 'quantity', 'total_price', 'flower', 'order_status_text',
                  'flower_text', 'flower_img', 'username','order_num']
        extra_kwargs = {
            'user': {'read_only': True},
            'total_price': {'read_only': True},
            'order_status': {'read_only': True},
        }
