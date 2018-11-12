from django.http import JsonResponse
from django.views import generic
from rest_framework import generics
from rest_framework import mixins

import time
import json

from . import models
from . import serializers


class InsuranceRiskList(generics.ListAPIView):
    queryset = models.InsuranceRisk.objects.all()
    serializer_class = serializers.InsuranceRiskListSerializer


class InsuranceRiskCreate(generics.CreateAPIView):
    queryset = models.InsuranceRisk.objects.all()
    serializer_class = serializers.InsuranceRiskSerializer


class InsuranceRiskCreateView(generic.View):

    def post(self, request, *args, **kwargs):
        print(json.loads(request.body.decode('utf-8')))
        return JsonResponse({'message': 'success'})


class ClientInsuranceRiskListView(generic.View):

    def get(self, request, *args, **kwargs):
        # time.sleep(2)
        insurance_risks = [{'id': x, 'name': 'My Risk ' + str(x)} for x in range(1, 11)]
        return JsonResponse(insurance_risks, safe=False)


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


class InsuranceRiskEditView(generic.View):

    def get(self, request, *args, **kwargs):
        insurance_risk = {
            'id': 1,
            'name': 'Insurance risk 1',
            'fields': [
                {
                    'id': 1,
                    'name': 'Field name String',
                    'type': 'text',
                    'value': 'Test string',
                },
                {
                    'id': 2,
                    'name': 'Field name Number',
                    'type': 'number',
                    'value': 666,
                },
                {
                    'name': 'Field name Enum',
                    'id': 3,
                    'type': 'select',
                    'value': 1,
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
