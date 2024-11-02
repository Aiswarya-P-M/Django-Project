from rest_framework import serializers
from .models import Departments
from app_School.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['sc_id', 'sc_name', 'location']


class DeptSerializer(serializers.ModelSerializer):
    schools = serializers.SerializerMethodField()

    class Meta:
        model = Departments
        fields = ['dept_id', 'dept_name', 'hod_name', 'schools']

    def get_schools(self, obj):
        # from app_School.serializers import SchoolSerializer
        # Get all schools related to the department
        schools = obj.school_departments_list.all()
        return SchoolSerializer(schools, many=True).data