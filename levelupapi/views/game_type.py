"""View module for handling requests about gametypes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up gametypes view"""
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of gametypes
        """
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single gametype

        Returns:
            Response -- JSON serialized gametype
        """
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for gametypes
    """
    class Meta:
        model = GameType
        fields = ('id', 'label',)