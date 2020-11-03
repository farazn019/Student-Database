from django.shortcuts import render, redirect, HttpResponseRedirect
from . forms import loginForm
from django.urls import re_path
from signUpPage.views import register
# from .models import <Insert whatever it is you want to import, but it might not be nexessary>


def login(request):
    if request.method == "POST":
        return redirect('signup')

        # form = loginForm(request.POST)
        # print("no nigga")
        if request.POST.get("signup"):
            # return render(request, 'homePage/homePage.html', {"form": form})
            # return redirect(re_path(r'^sigup$'))
            return register()
    else:
        form = loginForm(request.GET)
        return render(request, 'homePage/homePage.html', {"form": form})
