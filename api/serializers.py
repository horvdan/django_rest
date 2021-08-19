from api.models import Currency, Spending
from rest_framework import serializers

class SpendingSerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Spending 
        fields = ["date","amount","description","currency"]


    def create(self, validated_data):
        # HACK, currency should be in validated_data :(
        currency_code = self.context.get('request').data.get('currency')

        currency = Currency.objects.get(code=currency_code)        
        Spending.objects.create(currency=currency, **validated_data)

        return validated_data

    def update(self, validated_data):
        # TODO: try to figure out the serialization problem before implementing
        raise NotImplementedError()

