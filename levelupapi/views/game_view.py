"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game
from levelupapi.models import GameType
from levelupapi.models import Gamer


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

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        new_game = Game()
        new_game.gamer = Gamer.objects.get(user=request.auth.user)
        new_game.game_type = GameType.objects.get(pk=request.data['game_type'])
        new_game.title = request.data['title']
        new_game.number_of_players = request.data['number_of_players']
        new_game.skill_level = request.data['skill_level']
        new_game.maker = request.data['maker']
        new_game.save()

        serialized = GameSerializer(new_game, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data['title']
        game.maker = request.data['maker']
        game.number_of_players = request.data['number_of_players']
        game.skill_level = request.data['skill_level']

        game_type = GameType.objects.get(pk=request.data['game_type'])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'game_type', 'gamer', 'number_of_players', 'skill_level', 'maker',)
        depth = 2