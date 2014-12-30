from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from vphhf_rest.sms import views

urlpatterns = [
    url(r'^list/$', views.DocumentList.as_view(), name='file-list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.DocumentListDetail.as_view(), name='file-detail'),
    url(r'^list/(?P<pk>[0-9]+)/content/$', views.DocumentListContentDetail.as_view(), name='file-detail'),
  #  url(r'^list/documents/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/([a-z]{20})/$', views.DocumentListDetail.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)