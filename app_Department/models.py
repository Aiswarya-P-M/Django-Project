from django.db import models
# from app_School import models as school_model
# from App2 import models as Teacher_model
# Create your models here.
# from App2.models import Teacher


class ActiveManager(models.Manager):
    def  get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Departments(models.Model):
    hod_name=models.ForeignKey('app_Teacher.Teacher2',on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_name=models.CharField(max_length=100)
    dept_id=models.AutoField(primary_key=True)
    # sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True,related_name='school_departments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    objects = models.Manager()  # The default manager
    active_objects = ActiveManager() 

    # def __str__(self):
    #     return self.dept_name
    
#     def active_count(self):
#         return self.get_queryset().count()
    
#     def get_active(self):
#         return self.get_queryset().filter(is_active=True)
    
#     def get_inactive(self):
#         return self.get_queryset().filter(is_active=False)
    

    