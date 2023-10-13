from django.db import models

# Create your models here.
class student(models.Model):
    FName=models.CharField(max_length=200)
    LName=models.CharField(max_length=200)
    age=models.IntegerField()
    courses=models.CharField(max_length=200)

class course(models.Model):
    courseID=models.IntegerField()
    courseName=models.CharField(max_length=200)
    courseDesc=models.CharField(max_length=500)
   