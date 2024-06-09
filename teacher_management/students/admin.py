from django.contrib import admin
from .models import Student

# 注册学生模型到Admin后台
admin.site.register(Student)
