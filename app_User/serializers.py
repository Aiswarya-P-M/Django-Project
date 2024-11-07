from rest_framework import serializers
from .models import Users
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=["id","first_name","last_name","username","password","is_active","created_on","updated_on","is_admin","is_staff","is_superuser","role","performance","sc_id","department"]
        # extra_kwargs={
        #     'password':{'write_only':True}
        # }
    
    
    def create(self, validated_data):
        department=validated_data.pop('department', [])
        password=validated_data.pop('password')
        user=Users(**validated_data)
        user.set_password(password)
        user.save()
        user.department.set(department)
        return user