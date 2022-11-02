from django.db import models
from django.contrib.auth.models import User


class GamerEvent(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer', null=True, blank=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='event', null=True, blank=True)