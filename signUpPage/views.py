from django.shortcuts import render

# Created my view index here.
def index(request):
    return render(request, 'signUpPage/signUpPage.html')
