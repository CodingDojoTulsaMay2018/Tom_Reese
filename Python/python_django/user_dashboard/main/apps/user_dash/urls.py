from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^register$', views.register),
    url(r'^create$', views.create),
    url(r'^dashboard$', views.dash),
    url(r'^dashboard/admin$', views.dash_admin),
    url(r'^users/new$', views.new),
    url(r'^users/show/(?P<id>\d+)$', views.show),
    url(r'^show_post$', views.show_post),
    url(r'^comment$', views.comment),
    url(r'^users/edit/$', views.edit),
    url(r'^update$', views.update),
    url(r'^users/edit/(?P<id>\d+)$', views.edit_admin),
    url(r'^logoff$', views.logoff),

] 