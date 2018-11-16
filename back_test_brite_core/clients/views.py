from rest_framework import generics

from . import models
from . import serializers


class ClientInsuranceRiskList(generics.ListAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskListSerializer


class ClientInsuranceRiskCreate(generics.CreateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskCreateSerializer


class ClientInsuranceRiskRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return self.partial_update(request, *args, **kwargs)
