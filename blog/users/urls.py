# 开发者: 豆仔拌豆瓣
# 开发时间: 2022/5/6 18:47

 # 进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView
# 导入图片验证码视图路由
from users.views import ImageCodeView
from users.views import SmsCodeView
# 导入登录页面路由
from users.views import LoginView
# 导入退出登录页面路由
from users.views import LogoutView
# 导入忘记密码页面路由
from users.views import ForgetPasswordView


urlpatterns = [
    # path的第一个参数： 路由
    # path的第二个参数： 视图函数名
    path('register/',RegisterView.as_view(),name='register'),

    # 图片验证码的路由
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),

    # 短信发送
    path('smscode/',SmsCodeView.as_view(),name='smscode'),

    # 登录页面路由
    path('login/', LoginView.as_view(), name='login'),

    # 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),

    # 忘记密码路由引导
    path('forgetpassword/',ForgetPasswordView.as_view(),name='forgetpassword'),

]
