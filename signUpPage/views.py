from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
# Created my view index here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = RegisterForm()
    return render(response, 'signUpPage/signUpPage.html', {"form": form})


def index(request):
    return render(request, 'signUpPage/signUpPage.html')
