from django.contrib import admin

# Register your models here.
#把表导进来
from project_app.models import Project,Module
# Register your models here.
# django自带了一个admin后台
class ProjectAdmin(admin.ModelAdmin):
    list_display=['name','describe','status','create_time','id']

class ModuleAdmin(admin.ModelAdmin):
    list_display=['name','describe','create_time','id']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)
