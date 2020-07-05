from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = {
    url(r'^ask/', views.found),
    url(r'^answer/', views.found),
    url(r'^popular/', views.found),
    url(r'^new/', views.found),
    url(r'^', views.not_found),
    url(r'^question/(?P<num>\d+)/$', views.question),
    url(r'^$', views.found),
}