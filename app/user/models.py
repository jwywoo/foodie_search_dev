from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser?
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    favorites = []

# class User(AbstractUser):
    # pass
    # favorite_foods = models.ManyToManyField(
    #     'self',
    #     through='Relations',
    #     symmetrical=False,
    #     blank=True,
    #     related_name='from_relation_users',
    #     related_query_name='from_relation_user',
    # )
