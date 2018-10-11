from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
# 主要代码逻辑：

def index(request):

    return render(request,"index.html")
#处理登录请求
def login_action(request):
    if request.method=="POST":
        #username=request.GET.get("username")
        #password = request.GET.get("password")
        #修改为：如果用户没有值，初始化为空
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username=="" or password=="":
           #return HttpResponse("用户名或密码为空")
           return render(request, "index.html",
                         {"error":"用户名或密码错误"})
        else:
            user = auth.authenticate(
                username=username, password=password)
            #如果找不到对应的用户名密码，user的值就是空的，故不为空就代表取值正确
            if user is not None:
                auth.login(request, user) #记录用户登录状态，验证登录，登录成功才返回下面的页面
                return render(request, "project_manage.html")
            else:
                return render(request, "index.html",{"error": "用户名或密码错误"})
