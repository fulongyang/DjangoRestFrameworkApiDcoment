from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    like = models.CharField(max_length=100)

    class Meta:
        db_table = 'User_table'






