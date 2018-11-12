from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    url(
        r'^risk/(?P<pk>\d+)/$',
        csrf_exempt(views.ClientInsuranceRiskCreate.as_view()),
        name='client-insurance-risk-create',
    ),

    # url(r'^api/risk/create/$', csrf_exempt(views.InsuranceRiskCreateView.as_view()), name='insurance-risk-create'),

    # url(r'^api/client/risk/$', views.ClientInsuranceRiskListView.as_view(), name='client-insurance-risks'),
    # url(r'^api/client/risk/(?P<pk>\d+)/edit/$', csrf_exempt(views.InsuranceRiskEditView.as_view()), name='insurance-risk-edit'),
    # url(r'^admin/', admin.site.urls),
]
