from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from app_Teacher.models import Teacher2

# # Create your models here.




class Users(AbstractBaseUser):
    # emp_id = models.ForeignKey('app_Teacher.Teacher2', on_delete=models.DO_NOTHING, null=True, blank=True)  # Assuming this is the intended field
    USERNAME_FIELD = 'username'
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    role=models.CharField(max_length=50,null=True,blank=True)
    performance = models.FloatField(default=0)
    sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING, null=True, blank=True)
    department = models.ManyToManyField('app_Department.Departments', related_name='user_tea')

    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only hash the password if the user is new
            self.password = make_password(self.password)  # Hash the password
        super().save(*args, **kwargs)

