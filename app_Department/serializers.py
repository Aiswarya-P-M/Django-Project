from rest_framework import serializers
from .models import Departments
from app_School.models import School

class DeptSerializer(serializers.ModelSerializer):
    sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    class Meta:
        model = Departments
        fields = '__all__'