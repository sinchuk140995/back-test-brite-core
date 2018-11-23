from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^risk/$',
        views.InsuranceRiskListView.as_view(),
        name='insurance-risk-list',
    ),
    url(
        r'^risk/create/$',
        views.InsuranceRiskCreateView.as_view(),
        name='insurance-risk-create',
    ),
    url(
        r'^risk/(?P<pk>\d+)/$',
        views.InsuranceRiskRetrieveDestroyView.as_view(),
        name='insurance-risk-detail',
    ),
    url(
        r'^risk/(?P<pk>\d+)/delete/$',
        views.InsuranceRiskRetrieveDestroyView.as_view(),
        name='insurance-risk-delete',
    ),
    url(
        r'^field/(?P<pk>\d+)/delete/$',
        views.FieldDestroyView.as_view(),
        name='field-delete',
    ),
]
