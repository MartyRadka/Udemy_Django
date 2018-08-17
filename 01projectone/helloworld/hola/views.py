from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homePageViews(request):
    """Return what to do if I go to my homepage"""
    return HttpResponse('Hola means hello in Spanish')
