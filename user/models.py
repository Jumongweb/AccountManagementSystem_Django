from django.contrib.auth.models import AbstractUser
from django.db import models

from account.validator import validate_phone_number
from accountManagementSystem import settings


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True, validators=[validate_phone_number])


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
