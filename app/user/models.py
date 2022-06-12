from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


# AbstractUser?
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     favorites = []

class User(AbstractUser):
    email = models.EmailField(blank=True)
    food_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_food',
    )
