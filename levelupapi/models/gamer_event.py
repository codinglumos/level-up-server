from django.db import models
from django.contrib.auth.models import User


class GamerEvent(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='event', null=True, blank=True)