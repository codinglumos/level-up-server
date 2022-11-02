from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)