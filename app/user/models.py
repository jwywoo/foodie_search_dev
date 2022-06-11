from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser?
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     favorites = []

class User(AbstractUser):
    email = models.EmailField(blank=True)
    food_list = models.ManyToManyField(
        related_name='like_food',
        blank=True,
    )
