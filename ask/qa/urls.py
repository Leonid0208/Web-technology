from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = {
    url(r'^$', views.index),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/$', views.popular),
    url(r'^new/$', views.test),
    url(r'^question/(?P<num>\d+)/$', views.question),
}
