from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post),
    url(r'^process$', views.process),
    url(r'^wall$', views.wall),
    # url(r'^delete$', views.delete),
    url(r'^create$', views.create),
    url(r'^newuser$', views.newuser),
    url(r'^logout$', views.logout),
    url(r'^comment$', views.comment),
]