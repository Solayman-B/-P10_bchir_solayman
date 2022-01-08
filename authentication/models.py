from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
	username = models.CharField(max_length=99, unique=True)
	password = models.CharField(max_length=99)
	first_name = models.CharField(max_length=99)
	last_name = models.CharField(max_length=99)
	email = models.EmailField(max_length=99)
