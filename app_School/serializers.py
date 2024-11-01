from rest_framework import serializers
from .models import School
from app_Department.serializers import DeptSerializer


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'