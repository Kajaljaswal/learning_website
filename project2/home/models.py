from django.db import models


class student(models.Model):
      FName = models.CharField(max_length=200)
      LName = models.CharField(max_length=200)
      age= models.IntegerField()
      courses= models.CharField(max_length=100)



class subject(models.Model):
    subjectId = models.IntegerField()
    subjectName = models.CharField(max_length=200)
    subjectDescription = models.CharField(max_length=500)


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
class courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    add_date=models.DateField()
    image=models.ImageField(upload_to='images')   
    cate=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title   