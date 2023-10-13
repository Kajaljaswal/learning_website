from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.TextField()
    cpassword=models.TextField()

class Meta:
    model=User
    fields=('email','name','password','cpassword')
    
    
    
class user_login(models.Model):
 
    email=models.EmailField(max_length=100)
    password=models.TextField()
    
# class Meta:
#     model=User
#     fields=('email','password')