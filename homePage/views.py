from django.shortcuts import render, redirect
from . forms import loginForm
from signUpPage.views import register

def login(request):
    if request.method == "POST":
        return redirect('signup')

        if request.POST.get("signup"):
            return register()
    else:
        form = loginForm(request.GET)
        return render(request, 'homePage/homePage.html', {"form": form})
