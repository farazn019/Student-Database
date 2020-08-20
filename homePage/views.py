from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#from .models import <Insert whatever it is you want to import, but it might not be nexessary>

def index(request):
    return render(request, 'homePage/homePage.html')
