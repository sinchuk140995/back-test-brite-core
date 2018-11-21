from rest_framework import generics

from . import models
from . import serializers


class InsuranceRiskListView(generics.ListAPIView):
    queryset = models.InsuranceRisk.objects.all()
    serializer_class = serializers.InsuranceRiskListSerializer


class InsuranceRiskCreateView(generics.CreateAPIView):
    queryset = models.InsuranceRisk.objects.all()
    serializer_class = serializers.InsuranceRiskSerializer


class InsuranceRiskRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.InsuranceRiskSerializer
    queryset = models.InsuranceRisk.objects.all()
