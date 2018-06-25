from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^Remove$', views.remove),
    url(r'^wish_items/create$', views.create),
    url(r'^wish_items/(?P<id>\d+)$', views.items),
    url(r'^addwish$', views.addwish),
    url(r'^logoff$', views.logoff),
] 