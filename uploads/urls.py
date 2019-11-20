from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('nauka/', views.nauka, name='nauka'),
    url('info/', views.info, name='info'),
    url('quiz/', views.quiz, name='quiz'),
]
