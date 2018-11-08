from django.http import JsonResponse
from django.views import generic

import time


class InsuranceRiskListView(generic.View):

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        insurance_risks = [{'id': x, 'name': 'Risk ' + str(x)} for x in range(1, 11)]
        return JsonResponse(insurance_risks, safe=False)


class ClientInsuranceRiskListView(generic.View):

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        insurance_risks = [{'id': x, 'name': 'My Risk ' + str(x)} for x in range(1, 11)]
        return JsonResponse(insurance_risks, safe=False)
