from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = {
    url(r'^$', views.test),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/(?P<num>\d+)//$', views.question_famous),
    url(r'^new/$', views.test),
    url(r'^question/(?P<num>\d+)/$', views.question),
}