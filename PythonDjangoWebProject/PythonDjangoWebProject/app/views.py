"""
Definition of views for DjangoWebApplication/app.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from . import css
css.css('black', 'lime')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home page'
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About page'
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact page'
        }
    )

''' Error Pages '''

# Bad Request 
def handler400(request, template_name = 'app/error.html'):
    """Renders the 400 error page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        template_name,
        {
            'title':'400 error',
            'content': 'Bad Request',
        },
        status=400
    )

# Forbidden Error
def handler403(request, template_name = 'app/error.html'):
    """Renders the 403 error page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        template_name,
        {
            'title':'403 error',
            'content': 'Forbidden Error',
        },
        status=403
    )

# File Not Found 
def handler404(request, template_name = 'app/error.html'):
    """Renders the 404 error page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        template_name,
        {
            'title':'404 error',
            'content': 'File Not Found',
        },
        status=404
    )

# Internal Server Error
def handler500(request, template_name = 'app/error.html'):
    """Renders the 500 error page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        template_name,
        {
            'title':'500 error',
            'content': 'Internal Server Error',
        },
        status=500
    )