from django.db import models

# Create your models here.


class RegisterUser(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=80)
