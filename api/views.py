from rest_framework.routers import DefaultRouter
from api.serializers import SpendingSerializer
from api.models import Spending
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

class SpendingAPI(viewsets.ModelViewSet):
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['currency']