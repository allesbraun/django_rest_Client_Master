from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    """Listing clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']

