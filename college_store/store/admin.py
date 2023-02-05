from django.contrib import admin
from . models import Department,Course,User_details
# Register your models here.
class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_name']
admin.site.register(Department,DeptAdmin)
admin.site.register(Course)
admin.site.register(User_details)