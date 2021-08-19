from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseBadRequest
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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseBadRequest("Invalid currency")
