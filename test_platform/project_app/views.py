from django.shortcuts import render
from project_app.models import Project
from django.contrib.auth.decorators import   login_required

# Create your views here.
@login_required #判断用户是否登录
def project_manage(request):
    # 读取浏览器session
    username=request.session.get('user1','')
    project_all = Project.objects.all()
    print(project_all)
    return render(request, "project_manage.html",{
        "user":username,
        "projects":project_all,
        "type":"list"
    })

@login_required #判断用户是否登录
def add_project(request):
    """
       添加项目
    """
    return render(request, "project_manage.html",{"type":"add"})
