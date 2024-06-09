from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),  # 教师列表路径
    path('teacher/<int:teacher_id>/book/', views.book_appointment, name='book_appointment'),  # 预约教师路径
    path('search/', views.search_teachers, name='search_teachers'), #搜索教师路径
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),

]
