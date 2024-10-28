from django.db import models
from app_School.models import School  # Import School from the app_School app
from app_Department.models import Departments  # Import Department from the app_Department app
from app_Teacher.models import Teacher2

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)   

class Student1(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.AutoField(primary_key=True)
    maths=models.FloatField()
    chemistry=models.FloatField()
    physics=models.FloatField()
    total_marks=models.FloatField(editable=False)
    percentage=models.FloatField(editable=False)
    teacher_id = models.ForeignKey('app_Teacher.Teacher2', on_delete=models.DO_NOTHING,null=True,blank=True)
    sc_id = models.ForeignKey(School, on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id=models.ForeignKey(Departments, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    objects = models.Manager()  # The default manager
    active_objects = ActiveManager()

    
    def save(self, *args, **kwargs): 
        self.total_marks = self.maths + self.chemistry + self.physics
        self.percentage = (self.total_marks / 300) * 100
        super(Student1, self).save(*args, **kwargs) 

    


# class Teacher(models.Model):
#     name=models.CharField(max_length=50)
#     emp_id=models.AutoField(primary_key=True)
#     performance=models.FloatField(default=0)
#     created_on=models.DateTimeField(auto_now_add=True)
#     updated_on=models.DateTimeField(auto_now=True)
#     sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True)
#     dept_id=models.ForeignKey('app_Department.Departments', on_delete=models.DO_NOTHING, null=True, blank=True)
