"""
Definition of urls for login.
"""

from django.urls import path
from . import views

urlpatterns = [
    # login
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('load/', views.load, name='load'),
]


