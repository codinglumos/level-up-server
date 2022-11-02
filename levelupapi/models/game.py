from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='game_type', null=True, blank=True)
    title = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, null=True, blank=True)
    numberOfPlayers = models.IntegerField()
    skillLevel = models.IntegerField()
    maker = models.CharField(max_length=100)
    

