from rest_framework import serializers
from .models import *



class Teacherserializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"

class Student1serializers(serializers.ModelSerializer):
    teacher_id=serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())  # Allow write access
    class Meta:
        model = Student1
        fields = "__all__"