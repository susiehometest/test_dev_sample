from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 主要代码逻辑：

def index(request):

    return render(request,"index.html")
#处理登录请求
def login_action(request):
    if request.method=="GET":
        print(request.GET.get("username"))
