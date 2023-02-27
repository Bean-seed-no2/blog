# 进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView,ImageCodeView
from users.views import SmsCodeView,LoginView
from users.views import LogoutView,ForgetPasswordView
from users.views import UserCenterView,WriteBlogView

urlpatterns = [
    # path的第一个参数： 路由
    # path的第二个参数： 视图函数名
    path('register/',RegisterView.as_view(),name='register'),

    #图片验证码的路由
    path('imagecode/',ImageCodeView.as_view(),name='imagecode'),

    #短信发送
    path('smscode/',SmsCodeView.as_view(),name='smscode'),

    #登录路由
    path('login/',LoginView.as_view(),name='login'),

    #退出登录
    path('logout/',LogoutView.as_view(),name='logout'),

    #忘记密码
    path('forgetpassword/',ForgetPasswordView.as_view(),name='forgetpassword'),

    # 个人中心
    path('center/',UserCenterView.as_view(),name='center'),

    # 写博客的路由
    path('writeblog/',WriteBlogView.as_view(),name='writeblog'),
]