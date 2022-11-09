from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game', null=True, blank=True)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='organizer', null=True, blank=True)
    #attendees = models.ManyToManyField("Gamer", related_name='attendee')