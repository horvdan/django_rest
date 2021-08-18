from api.models import Spending
from rest_framework import serializers

class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending 
        fields = "__all__"
