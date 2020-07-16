"""
Definition of urls for PythonDjangoWebProject/app.
"""

from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('about/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('', views.about, name='about'),
    path('400/', views.handler400, name='400'),
    path('403/', views.handler403, name='403'),
    path('404/', views.handler404, name='404'),
    path('500/', views.handler500, name='500'),
]