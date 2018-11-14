from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    url(
        r'^risk/$',
        views.InsuranceRiskList.as_view(),
        name='insurance-risk-list',
    ),

    url(
        r'^risk/create/$',
        views.InsuranceRiskCreate.as_view(),
        name='insurance-risk-create',
    ),

    url(
        r'^risk/(?P<pk>\d+)/$',
        views.InsuranceRiskRetrieve.as_view(),
        name='insurance-risk-detail',
    ),

    # url(
    #     r'^risk/test/(?P<pk>\d+)/$',
    #     views.TestInsuranceRiskRetrieve.as_view(),
    #     name='insurance-risk-detail',
    # ),
]
