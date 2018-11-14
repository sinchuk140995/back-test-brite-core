from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class ClientInsuranceRiskList(generics.ListAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskListSerializer


class ClientInsuranceRiskCreate(generics.CreateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer


class ClientInsuranceRiskRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer


# class ClientInsuranceRiskUpdate(generics.UpdateAPIView):
#     queryset = models.ClientInsuranceRisk.objects.all()
#     serializer_class = serializers.ClientInsuranceRiskSerializer


# class TestClientInsuranceRiskRetrieve(generics.RetrieveAPIView):
#     queryset = models.ClientInsuranceRisk.objects.all()
#     serializer_class = serializers.ClientInsuranceRiskSerializer


# class ClientInsuranceRiskRetrieve(APIView):

#     def get(self, request, format=None, *args, **kwargs):
#         try:
#             client_insurance_risk = models.ClientInsuranceRisk.objects.get(pk=kwargs['pk'])
#         except models.ClientInsuranceRisk.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         risk_fields = []
#         for client_field in client_insurance_risk.fields.all():
#             field_data = {
#                 'id': client_field.pk,
#                 'field': client_field.field.pk,
#                 'name': client_field.field.name,
#                 'field_type': client_field.field.field_type,
#             }

#             if client_field.field.field_type == client_field.field.SELECT:
#                 options = []
#                 for option in client_field.field.options.all():
#                     options.append({
#                         'id': option.id,
#                         'name': option.name,
#                     })
#                 field_data['options'] = options
#                 field_data['select_option'] = client_field.select_option.pk
#             else:
#                 field_data['value'] = client_field.value

#             risk_fields.append(field_data)

#         insurance_data = {
#             'insurance_risk': client_field.field.insurance_risk.id,
#             'name': client_field.field.insurance_risk.name,
#             'fields': risk_fields,
#         }

#         return Response(insurance_data)
