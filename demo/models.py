from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    weight = models.IntegerField()
    gender = models.CharField(choices=[('male','male'),('male','female')],max_length=10,default='female')