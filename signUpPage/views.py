from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
# Created my view index here.




def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        print("Username: " + username + "\nPassword: " + password + "\nEmail: " + email)

        if form.is_valid():
            form.save(commit=True)
    else:
        form = RegisterForm()
    return render(request, 'signUpPage/signUpPage.html', {"form": form})


def index(request):
    return render(request, 'signUpPage/signUpPage.html')
