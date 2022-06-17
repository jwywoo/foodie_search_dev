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
    # liked_food = models.ManyToManyField(
    #     'self',
    #     through='Like',
    #     symmetrical=True,
    #     blank=True,
    # )


# class Like(models.Model):
#     user_liked = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='user_like'
#     )
#     food_liked = models.ForeignKey(
#         Food,
#         on_delete=models.CASCADE,
#         related_name='food_liked'
#     )
