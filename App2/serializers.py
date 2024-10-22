from rest_framework import serializers
from .models import *

class Student1serializers(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = "__all__"

class Teacherserializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"