from django.db import models
from app_School.models import School  # Import School from the app_School app
from app_Department.models import Departments  # Import Department from the app_Department app
# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)   

class Teacher2(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.AutoField(primary_key=True)
    performance=models.FloatField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    department=models.ManyToManyField('app_Department.Departments',related_name='teacher_list') 

    objects = models.Manager()  # The default manager
    active_objects = ActiveManager()

    
