from django.db import models


class UserInfo(models.Model):
    """ 用户表 """
    sex_choices = (
        (0, '女'),
        (1, '男'),
    )
    role_choices = (
        (1, '普通用户'),
        (2, '管理员'),
    )
    role = models.IntegerField(verbose_name='角色', choices=role_choices, default=1)
    username = models.CharField(verbose_name='用户名', max_length=16, unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    name = models.CharField(verbose_name='姓名', max_length=32)
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices, default=1)
    avatar = models.CharField(verbose_name='头像', max_length=1000, default='')
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True, db_index=True)
    addr = models.CharField(verbose_name='地址', max_length=255, default='')
    create_time = models.DateTimeField(verbose_name='用户新增时间', auto_now_add=True)

    class Meta:
        db_table = 'db_userinfo'


class Flower(models.Model):
    """ 鲜花表 """
    name = models.CharField(verbose_name='鲜花名称', max_length=64)
    stock = models.IntegerField(verbose_name='鲜花库存量', default=1000)
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)
    image = models.TextField(verbose_name='图片地址', default='')
    flower_language = models.CharField(verbose_name='花语', max_length=255)
    create_time = models.DateTimeField(verbose_name='鲜花新增时间', auto_now_add=True)

    class Meta:
        db_table = 'db_flower'


class Order(models.Model):
    """ 订单表 """
    order_choices = (
        (1, '待审核'),
        (2, '已完成'),
    )
    user = models.ForeignKey(verbose_name='用户id', to='UserInfo', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='下单时间', auto_now_add=True)
    flower = models.ForeignKey(verbose_name='鲜花id', to='Flower', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='购买数量', default=0)
    total_price = models.DecimalField(verbose_name='总价格', max_digits=10, decimal_places=2)
    order_status = models.IntegerField(verbose_name='订单状态', choices=order_choices, default=2)
    order_num = models.CharField(verbose_name='订单号', max_length=255, default='')

    class Meta:
        db_table = 'db_order'


class OrderReview(models.Model):
    """ 订单审核表 """
    user = models.ForeignKey(verbose_name='用户id', to='UserInfo', on_delete=models.CASCADE)
    order = models.ForeignKey(verbose_name='订单id', to='Order', on_delete=models.CASCADE)
    order_review_time = models.DateTimeField(verbose_name='订单审核时间', auto_now_add=True)


class Announcement(models.Model):
    """ 公告表 """
    title = models.CharField(verbose_name='公告标题', max_length=64)
    content = models.CharField(verbose_name='公告内容', max_length=1000)
    user = models.ForeignKey(verbose_name='用户id', to='UserInfo', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'db_announcement'


class Banner(models.Model):
    """ 轮播图表 """
    image = models.TextField(verbose_name='图片地址', default='')
    user = models.ForeignKey(verbose_name='用户id', to='UserInfo', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'db_banner'
