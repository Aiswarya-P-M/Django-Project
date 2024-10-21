from rest_framework import serializers
from .models import *

class Student1serializers(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = "__all__"