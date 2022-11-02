from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game', null=True, blank=True)
    description = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user', null=True, blank=True)
