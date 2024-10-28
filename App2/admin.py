from django.contrib import admin
from .models import *
# Register your models here.
# @admin.register(Student1)
# class Student1Admin(admin.ModelAdmin):
#     list_display = ('name', 'rollno', 'maths', 'chemistry', 'physics', 'total_marks', 'percentage', 'classteacher')
#     readonly_fields = ('total_marks', 'percentage')
admin.site.register(Student1)
# admin.site.register(Teacher)