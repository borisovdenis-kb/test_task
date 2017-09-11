from django.conf.urls import url
from APIs.partnersApi import partnersApi


urlpatterns = [
    url(r'^partners/worksheets/$', partnersApi.WorksheetsList.as_view()),
    url(r'^partners/worksheets/(?P<pk>\d+)/$', partnersApi.WorksheetsDetail.as_view()),
    url(r'^partners/claims/(?P<pk>\d+)/send$', partnersApi.SendClaim.as_view()),
]
