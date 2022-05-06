# 开发者: 豆仔拌豆瓣
# 开发时间: 2022/5/6 20:52


from django.urls import path
from home.views import IndexView    # 导入index首页视图
urlpatterns = [
    # 首页的路由
    path('',IndexView.as_view(),name='index'),

]