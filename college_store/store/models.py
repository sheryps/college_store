from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_details(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     Name = models.CharField(max_length=220)
     DOB = models.DateField()
     Age=models.IntegerField()    
     Gender = models.CharField(max_length=20)
     phone=models.IntegerField()
     Email=models.EmailField(max_length=220)
     Address = models.CharField(max_length=220)
     Department=models.CharField(max_length=50)
     course=models.CharField(max_length=50)
     purpose=models.CharField(max_length=50)
     Materials=models.CharField(max_length=100)

class Department(models.Model):
    dept_name=models.CharField(max_length=225)   

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)    
    course=models.CharField(max_length=225)

    def __str__(self):
        return self.course