from django.contrib import admin
from .models import Teacher, Schedule, Appointment

# 注册教师模型到Admin后台
admin.site.register(Teacher)
# 注册教师日程模型到Admin后台
admin.site.register(Schedule)
# 注册预约模型到Admin后台
admin.site.register(Appointment)
