from django.db import models




# 教师模型
class Teacher(models.Model):
    name = models.CharField(max_length=100)  # 教师姓名
    where = models.TextField() #领域
    education_background = models.TextField()  # 教育背景
    work_experience = models.TextField()  # 工作经历
    research_achievements = models.TextField()  # 科研成果

    def __str__(self):
        return f"{self.name}, 方向: {self.where}"

# 教师日程模型
class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # 外键关联到教师
    date = models.DateField()  # 日期
    available_time_slots = models.JSONField()  # 可预约时间段（例：{"09:00-10:00": True, "10:00-11:00": False}）

    def __str__(self):
        return f"{self.teacher.name} - {self.date} - {self.available_time_slots}"

# 预约模型
class Appointment(models.Model):
    student_name = models.CharField(max_length=100)  # 学生姓名
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # 外键关联到教师
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)  # 外键关联到日程
    time_slot = models.CharField(max_length=20)  # 时间段（例："09:00-10:00"）

    def __str__(self):
        return f"{self.student_name} - {self.teacher.name} - {self.time_slot}"
