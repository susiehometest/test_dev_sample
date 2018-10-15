from django.db import models

# Create your models here.
# ORM 创建数据库表
#class=table user_app_project
#变量 =字段(类型、长度),默认创建表会要加的id,create_time
#数据类型查看，在(python安装包下):D:\python\Python37\Lib\site-packages\django\db\models\fields\_init_.py
class Project(models.Model):
    """
    项目表
    """
    # 字符长100，默认为空default="",null=true,代表该字段允许为空，blank=True,代表表单可以不填
    name=models.CharField("名称",max_length=100,blank=False,default="")
    describe=models.TextField("描述",default="")
    status=models.BooleanField("状态：",default=True)
    create_time=models.DateTimeField("创建时间",auto_now=True)

class Module(models.Model):
    """
    模块表:
    """
    #模块关联项目,如果项目被删除，模块是否需要保留on_delete=models.CASCADE代表一块被删除
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    name=models.CharField("名称",max_length=100,blank=False,default="")
    describe=models.TextField("描述",default="")
    create_time = models.DateTimeField("创建时间",auto_now=True)