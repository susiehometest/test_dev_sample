from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
#引用登陆访问授权
from django.contrib.auth.decorators import login_required

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
                auth.login(request,user)#记录用户登录状态
                #将session记录到浏览器中
                request.session['user1']=username
                return HttpResponseRedirect('/manage/project_manage/')
            else:
                return render(request, "index.html",{"error": "用户名或密码错误"})


#增加logout视图
def logout(request):
    auth.logout(request) #清除用户的登录状态
    response=HttpResponseRedirect('/')#退出后跳转到登录页
    return response