from rest_framework.filters import OrderingFilter
from api.serializers import SpendingSerializer
from api.models import Spending
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

class SpendingAPI(viewsets.ModelViewSet):
    queryset = Spending.objects.all()
    serializer_class = SpendingSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['currency']
    ordering_fields = ['amount']
