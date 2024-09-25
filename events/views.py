from rest_framework.permissions import AllowAny  # remove after
from rest_framework import viewsets
from .models import Events
from .serializers import EventSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]