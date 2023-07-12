from rest_framework import viewsets
from clients.serializers import ClientSerializer
from clients.models import Client

class ClientsViewSet(viewsets.ModelViewSet):
    """Listing clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

