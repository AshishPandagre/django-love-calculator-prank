from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
import random

def generate_key():
	return ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])


class User(AbstractUser):
    key = models.CharField(default=generate_key, max_length=14)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Referral(models.Model):
    _from = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='ref_from')
    name = models.CharField(max_length=20, blank=True, null=True)
    crush = models.CharField(max_length=20, blank=True, null=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    comment = models.TextField()
