"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer


class EventView(ViewSet):
    """Level up events view"""
    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
            """Handle POST operations

            Returns
                Response -- JSON serialized event instance
            """
            new_event = Event()
            new_event.game = Game.objects.get(pk=request.data['game'])
            new_event.description = request.data['description']
            new_event.organizer = Gamer.objects.get(user=request.auth.user)
            new_event.save()

            serialized = EventSerializer(new_event, many=False)

            return Response(serialized.data, status=status.HTTP_201_CREATED)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer',)