from django.db import models
# Create your models here.
class Student1(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField(primary_key=True)
    maths=models.FloatField()
    chemistry=models.FloatField()
    physics=models.FloatField()
    total_marks=models.FloatField(editable=False)
    percentage=models.FloatField(editable=False)
    # classteacher=models.CharField(max_length=50, null=True, blank=True)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING,null=True,blank=True)
    
    def save(self, *args, **kwargs): 
        self.total_marks = self.maths + self.chemistry + self.physics
        self.percentage = (self.total_marks / 300) * 100
        super(Student1, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.IntegerField(primary_key=True)
    performance=models.FloatField(default=0)
