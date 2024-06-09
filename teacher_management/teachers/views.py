from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Schedule, Appointment
from .form import TeacherSearchForm
from django.db import models

# 教师列表视图
def teacher_list(request):
    query = request.GET.get('q')  # 获取搜索查询参数
    if query:
        teachers = Teacher.objects.filter(name__icontains=query)  # 按名称过滤教师
    else:
        teachers = Teacher.objects.all()  # 获取所有教师
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

# 预约教师视图
def book_appointment(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)  # 获取指定ID的教师
    if request.method == 'POST':
        student_name = request.POST['student_name']  # 获取表单中的学生姓名
        schedule_id = request.POST['schedule_id']  # 获取表单中的日程ID
        time_slot = request.POST['time_slot']  # 获取表单中的时间段
        schedule = get_object_or_404(Schedule, id=schedule_id)  # 获取指定ID的日程
        Appointment.objects.create(student_name=student_name, teacher=teacher, schedule=schedule, time_slot=time_slot)  # 创建预约
        return redirect('teacher_detail', teacher_id=teacher_id)  # 重定向到教师详情页
    schedules = Schedule.objects.filter(teacher=teacher)  # 获取教师的所有日程
    return render(request, 'teachers/book_appointment.html', {'teacher': teacher, 'schedules': schedules})

# teachers/views.py
def search_teachers(request):
    form = TeacherSearchForm(request.GET or None)
    teachers = Teacher.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            teachers = teachers.filter(
                models.Q(name__icontains=query) |
                models.Q(education_background__icontains=query) |
                models.Q(work_experience__icontains=query) |
                models.Q(research_achievements__icontains=query)
            )

    context = {
        'form': form,
        'teachers': teachers,
    }
    return render(request, 'teachers/search_results.html', context)



# teachers/views.py
def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})

