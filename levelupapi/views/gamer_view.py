"""View module for handling requests about gamers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models.gamer import Gamer


class GamerView(ViewSet):
    """Level up gamers view"""
    def list(self, request):
        """Handle GET requests to get all gamers

        Returns:
            Response -- JSON serialized list of gamers
        """
        gamers = Gamer.objects.all()
        serializer = GameSerializer(gamers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single gamer

        Returns:
            Response -- JSON serialized gamer
        """
        gamer = Gamer.objects.get(pk=pk)
        serializer = GameSerializer(gamer, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers
    """
    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio',)