from django.conf.urls import url
from APIs.partnersApi import partnersApi


urlpatterns = [
    url(r'^partners/worksheets/$', partnersApi.worksheets_list),
    url(r'^partners/worksheets/(?P<pk>\d+)/$', partnersApi.worksheets_detail),
    url(r'^partners/claims/(?P<pk>\d+)/send$', partnersApi.send_claim),
]
