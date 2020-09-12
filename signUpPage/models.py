from django.db import models
from django.contrib.auth.models import User


def new_user(email, username, password):
    user = User.objects.create_user(username, email, password, )


# Create your models here.
