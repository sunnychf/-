from django.db import models
from teachers.models import Teacher

# 学生模型
class Student(models.Model):
    name = models.CharField(max_length=100)  # 学生姓名
    chosen_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)  # 外键关联到教师

    def __str__(self):
        return self.name
