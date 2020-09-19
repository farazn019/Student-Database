from django.shortcuts import render
from . forms import loginForm
# from .models import <Insert whatever it is you want to import, but it might not be nexessary>


def login(response):
    if response.method == "POST":
        form = loginForm(response.POST)
    else:
        form = loginForm(response.POST)
    return render(response, 'homePage/homePage.html', {"form": form})
