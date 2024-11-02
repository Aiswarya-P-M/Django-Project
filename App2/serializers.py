from rest_framework import serializers
from .models import *
from app_School.models import School
from app_Department.models import Departments



# class Teacherserializers(serializers.ModelSerializer):
#     sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
#     dept_id = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all())
#     class Meta:
#         model=Teacher
#         fields="__all__"
class Student1serializers(serializers.ModelSerializer):
    teacher_id=serializers.PrimaryKeyRelatedField(queryset=Teacher2.objects.all())  # Allow write access
    class Meta:
        model = Student1
        fields = "__all__"
