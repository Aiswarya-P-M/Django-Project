from rest_framework import serializers
from .models import *
from app_School.models import School
from app_Department.models import Departments



class Teacher2serializers(serializers.ModelSerializer):
    sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    dept_id = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all())
    class Meta:
        model=Teacher2
        fields="__all__"