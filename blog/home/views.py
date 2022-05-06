from django.shortcuts import render

from django.views import View

# Create your views here.

# 定义首页视图
class IndexView(View):
    def get(self,request):

        return render(request,'index.html')