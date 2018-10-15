from django.contrib import admin
#把表导进来
from user_app.models import Project,Module
# Register your models here.
# django自带了一个admin后台
admin.site.register(Project)
admin.site.register(Module)
