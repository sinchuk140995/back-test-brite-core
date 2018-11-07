from django.http import JsonResponse
from django.views import generic


class InsuranceRiskListView(generic.View):

    def get(self, request, *args, **kwargs):
        insurance_risks = [{'id': x, 'name': 'Risk ' + str(x)} for x in range(1, 11)]
        return JsonResponse(insurance_risks, safe=False)
