from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from teachers.models import Teacher

# 选择导师视图
def choose_teacher(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # 获取指定ID的学生
    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']  # 获取表单中的教师ID
        teacher = get_object_or_404(Teacher, id=teacher_id)  # 获取指定ID的教师
        student.chosen_teacher = teacher  # 设置学生选择的导师
        student.save()  # 保存学生信息
        return redirect('student_detail', student_id=student_id)  # 重定向到学生详情页
    teachers = Teacher.objects.all()  # 获取所有教师
    return render(request, 'students/choose_teacher.html', {'student': student, 'teachers': teachers})
