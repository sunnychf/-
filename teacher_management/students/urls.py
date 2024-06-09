from django.urls import path
from . import views

urlpatterns = [
    path('<int:student_id>/choose_teacher/', views.choose_teacher, name='choose_teacher'),  # 选择导师路径
]
