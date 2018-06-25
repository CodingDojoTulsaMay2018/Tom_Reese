from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^profile$', views.profile),
    url(r'^secrets$', views.secrets),
    url(r'^secret$', views.secret),
    url(r'^like$', views.like), 
    url(r'^delete$', views.delete),
    url(r'^logoff$', views.logoff),
] 