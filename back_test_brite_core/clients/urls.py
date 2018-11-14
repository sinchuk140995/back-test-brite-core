from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    url(
        r'^risk/$',
        views.ClientInsuranceRiskList.as_view(),
        name='client-insurance-risks',
    ),
    url(
        r'^risk/create/$',
        # r'^risk/(?P<pk>\d+)/$',
        csrf_exempt(views.ClientInsuranceRiskCreate.as_view()),
        name='client-insurance-risk-create',
    ),
    url(
        r'^risk/(?P<pk>\d+)/$',
        csrf_exempt(views.ClientInsuranceRiskRetrieveUpdate.as_view()),
        name='client-insurance-risk-retrieve',
    ),
    url(
        r'^risk/(?P<pk>\d+)/edit/$',
        csrf_exempt(views.ClientInsuranceRiskRetrieveUpdate.as_view()),
        name='client-insurance-risk-edit',
    ),
    # url(
    #     r'^risk/test/(?P<pk>\d+)/$',
    #     csrf_exempt(views.ClientInsuranceRiskRetrieve.as_view()),
    #     name='client-insurance-risk-retrieve',
    # ),
]
