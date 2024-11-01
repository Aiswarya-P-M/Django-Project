from rest_framework import serializers
from .models import *
from app_School.models import School
from app_Department.models import Departments



class Teacher2serializers(serializers.ModelSerializer):
    sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    department = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all(), many=True)

    class Meta:
        model = Teacher2
        fields = "__all__"

    def validate(self, data):
        school = data.get('sc_id')
        departments = data.get('department', [])
        valid_departments = Departments.objects.filter(sc_id=school)
        # Validate that each department belongs to the selected school
        for department in departments:
            if department not in valid_departments:
                raise serializers.ValidationError(
                    f"The department '{department.dept_name}' is not under the selected school '{school.sc_name}'."
                )

        return data

