from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^quotes$', views.quotes),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^like$', views.like), 
    url(r'^user/(?P<id>\d+)$', views.user_quotes),
    url(r'^delete$', views.delete),
    url(r'^logoff$', views.logoff),
] 