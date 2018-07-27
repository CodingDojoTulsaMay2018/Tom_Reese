from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^profile$', views.profile),
    url(r'^roster$', views.roster),
    # url(r'^auction$', views.auction),
    url(r'^update$', views.update),
    url(r'^find_player$', views.find_player), 
    url(r'manager_stats$', views.manager_stats),
    url(r'^message_text$', views.message_text),
    url(r'^logoff$', views.logoff),
] 