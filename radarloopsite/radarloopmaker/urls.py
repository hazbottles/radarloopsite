from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^locationfromID/(?P<ID>\w+)/$', views.locationfromID, name='locationfromID'),
    url(r'^makegiftolatest/$', views.makegiftolatest, name='makegiftolatest'),
]