from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password
# # Create your models here.




class Users(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only hash the password if the user is new
            self.password = make_password(self.password)  # Hash the password
        super().save(*args, **kwargs)

