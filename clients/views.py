from rest_framework import generics

from . import models
from . import serializers


class ClientInsuranceRiskListView(generics.ListAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskListSerializer


class ClientInsuranceRiskCreateView(generics.CreateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskCreateSerializer


class ClientInsuranceRiskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer
