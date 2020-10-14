from django.shortcuts import render, redirect, HttpResponseRedirect
from . forms import loginForm
# from .models import <Insert whatever it is you want to import, but it might not be nexessary>


def login(response):
    if response.method == "POST":
        if response.POST.get("signup"):
            return HttpResponseRedirect(redirect("signup.view"))
    else:
        form = loginForm(response.POST)
        return render(response, 'homePage/homePage.html', {"form": form})
