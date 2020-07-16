"""
Definition of urls for PythonDjangoWebProject.
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('',include('app.urls')),
    path('login/',include('login.urls')),
    path('admin/', admin.site.urls),
]

handler400 = 'app.views.handler400'
handler403 = 'app.views.handler403'
handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'
