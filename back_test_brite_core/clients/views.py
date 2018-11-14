from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

import json

from . import models
from . import serializers


class ClientInsuranceRiskList(generics.ListAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskListSerializer


class ClientInsuranceRiskCreate(generics.CreateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ClientInsuranceRiskUpdate(generics.UpdateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer

    def put(self, request, *args, **kwargs):
        print(request.data)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return self.partial_update(request, *args, **kwargs)


class ClientInsuranceRiskRetrieve(APIView):

    def get(self, request, format=None, *args, **kwargs):
        try:
            client_insurance_risk = models.ClientInsuranceRisk.objects.get(pk=kwargs['pk'])
        except models.ClientInsuranceRisk.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        risk_fields = []
        for client_field in client_insurance_risk.fields.all():
            field_data = {
                'id': client_field.pk,
                'field': client_field.field.pk,
                'name': client_field.field.name,
                'field_type': client_field.field.field_type,
            }

            if client_field.field.field_type == client_field.field.SELECT:
                options = []
                for option in client_field.field.options.all():
                    options.append({
                        'id': option.id,
                        'name': option.name,
                    })
                field_data['options'] = options
                field_data['select_option'] = client_field.select_option.pk
            else:
                field_data['value'] = client_field.value

            risk_fields.append(field_data)

        insurance_data = {
            'insurance_risk': client_field.field.insurance_risk.id,
            'name': client_field.field.insurance_risk.name,
            'fields': risk_fields,
        }

        return Response(insurance_data)


class InsuranceRiskTakeView(generic.View):

    def get(self, request, *args, **kwargs):
        insurance_risk = {
            'id': 1,
            'name': 'Insurance risk 1',
            'fields': [
                {'id': 1, 'name': 'Field name String', 'type': 'text'},
                {'id': 2, 'name': 'Field name Number', 'type': 'number'},
                {
                    'name': 'Field name Enum',
                    'id': 3,
                    'type': 'select',
                    'options': [
                        {'id': 1, 'name': 'Option 1'},
                        {'id': 2, 'name': 'Option 2'},
                        {'id': 3, 'name': 'Option 3'},
                    ],
                },
            ]
        }
        return JsonResponse(insurance_risk)

    def post(self, request, *args, **kwargs):
        time.sleep(2)
        print(json.loads(request.body.decode('utf-8')))
        return JsonResponse({'message': 'success'})
