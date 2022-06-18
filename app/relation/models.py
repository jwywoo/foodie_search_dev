from django.db import models
from user.models import User
from food.models import Food


class Relation(models.Model):
    user_like = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_like"
    )
    food_liked = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name="food_liked"
    )
