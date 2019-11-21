from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('nauka/', views.nauka, name='nauka'),
    url('info/', views.info, name='info'),
    url('quiz/', views.quiz, name='quiz'),
    url('tales/', views.tales, name='tales'),
    url('anaksymander/', views.anaksymander, name='anaksymander'),
    url('anaksymenes/', views.anaksymenes, name='anaksymenes'),
    url('heraklit/', views.heraklit, name='heraklit'),
    url('pitagoras/', views.pitagoras, name='pitagoras'),
    url('parmenides/', views.parmenides, name='parmenides'),
    url('empedokles/', views.empedokles, name='empedokles'),
    url('anaksagoras/', views.anaksagoras, name='anaksagoras'),
    url('demokryt/', views.demokryt, name='demokryt')
]
