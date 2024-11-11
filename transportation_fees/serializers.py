from rest_framework import serializers
from .models import TransportationFee


class TransportationFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationFee
        fields = '__all__'
