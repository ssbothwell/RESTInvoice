from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from invoices import views

urlpatterns = [
    url(r'^invoices/$', views.InvoiceList.as_view()),
    url(r'^invoices/(?P<pk>[0-9]+)/$', views.InvoiceDetail.as_view()),
    url(r'^lineitems/$', views.LineItemList.as_view()),
    url(r'^lineitems/(?P<pk>[0-9]+)/$', views.LineItemDetail.as_view()),
    url(r'^clients/$', views.ClientList.as_view()),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

