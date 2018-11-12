from django.shortcuts import render
from django.views import generic
from rest_framework import generics

import json

from . import models
from . import serializers


class ClientInsuranceRiskCreate(generics.CreateAPIView):
    queryset = models.ClientInsuranceRisk.objects.all()
    serializer_class = serializers.ClientInsuranceRiskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
