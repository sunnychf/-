# teachers/forms.py
from django import forms

class TeacherSearchForm(forms.Form):
    query = forms.CharField(label='搜索教师', max_length=100, required=False)
