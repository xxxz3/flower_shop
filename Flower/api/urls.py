from django.urls import path
from rest_framework import routers

from api import views

router = routers.SimpleRouter()

# 用户注册
router.register(r'register', views.RegisterView, 'register')

# 鲜花
router.register(r'flower', views.FlowerView, 'flower')

# 用户
router.register(r'user', views.UserView, 'user')

# 公告
router.register(r'announcement', views.AnnouncementView, 'announcement')

# 轮播图
router.register(r'banner', views.BannerView, 'banner')

# 订单管理
router.register(r'order', views.OrderView, 'order')


urlpatterns = [
    # 用户登录
    path('login/', views.LoginView.as_view())
]

urlpatterns += router.urls
