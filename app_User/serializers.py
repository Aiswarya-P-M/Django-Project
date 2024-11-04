from rest_framework import serializers
from .models import Users
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"

    def validate_password(self, value):
        try:
            # Validate the password using Django's built-in validators
            validate_password(value)
        except ValidationError as e:
            # Raise validation error with a specific message if password fails validation
            raise serializers.ValidationError(e.messages)
        return value