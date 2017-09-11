from django.conf.urls import url
from APIs.creditOrgApi import creditOrgApi


urlpatterns = [
    # url(r'^creditorg/claims$', creditOrgApi.claims_list),
    url(r'^creditorg/claims/$', creditOrgApi.ClaimsList.as_view()),
    url(r'^creditorg/claims/(?P<pk>\d+)/$', creditOrgApi.ClaimsDetail.as_view()),
    url(r'^creditorg/offers/$', creditOrgApi.offers_list),
    url(r'^creditorg/offers/(?P<pk>\d+)/$', creditOrgApi.offers_detail),
]
