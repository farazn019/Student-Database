from django.urls import re_path
from django.shortcuts import redirect
import signUpPage.views
from . import views


urlpatterns = [
    re_path(r'^$', views.login, name='login'),
    re_path('signUpPage', signUpPage.views.register, name='signup')
    # re_path('')
]
