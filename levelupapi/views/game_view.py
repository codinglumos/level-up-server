"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):
    """Level up games view"""
    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'game_type', 'gamer', 'number_of_players', 'skill_level', 'maker',)