from django.db import models
from app_School.models import School  # Import School from the app_School app
from app_Department.models import Departments  # Import Department from the app_Department app

# Create your models here.
class Teacher2(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.AutoField(primary_key=True)
    performance=models.FloatField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id=models.ForeignKey('app_Department.Departments', on_delete=models.DO_NOTHING, null=True, blank=True)

    