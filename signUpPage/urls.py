from django.urls import re_path
from . import views

app_name='signup'

urlpatterns=[
    re_path('^$', views.register, name=app_name),
]