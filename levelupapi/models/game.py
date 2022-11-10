from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='game_type', null=True, blank=True)
    title = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamers', null=True, blank=True)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    maker = models.CharField(max_length=100)
    

