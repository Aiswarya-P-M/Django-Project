from django.db import models
# from app_Department import models as department_models
# Create your models here.

class School(models.Model):
    sc_name=models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sc_id=models.AutoField(primary_key=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
