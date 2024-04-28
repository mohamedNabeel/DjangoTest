from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customuser(AbstractUser):
    name = models.CharField(max_length=95)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    role = models.BinaryField()
