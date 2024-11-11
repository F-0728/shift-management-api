from rest_framework import viewsets
from .models import TransportationFee
from .serializers import TransportationFeeSerializer

class TransportationFeeViewSet(viewsets.ModelViewSet):

    queryset = TransportationFee.objects.all()
    serializer_class = TransportationFeeSerializer
