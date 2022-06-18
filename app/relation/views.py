from django.shortcuts import render

from food.models import Food
from user.models import User
from relation.models import Relation


# creating relation instance between user and food with given food_pk and request.user
def add_favorite_food(request, pk):
    if request.method == 'POST':
        print(request.user.pk)
        print(type(request.user.pk))
        user = User.objects.get(pk=request.user.pk)
        food = Food.objects.get(pk=pk)
        relation = Relation.objects.create(user_like=user, food_liked=food)
        relation.save()
    return render(request, 'food/main.html')


# removing relation instance between user and food with given food_pk and request.user
def remove_favorite_food(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        food = Food.objects.get(pk=pk)
        Relation.objects.delete(user_like=user, food_liked=food)
    return render(request, 'user/user_detail.html')


def user_list(request):
    user = User.objects.get(pk=request.user.pk)
    liked_relation = Relation.objects.filter(user_like=user)
    liked_food = []
    for i in liked_relation:
        liked_food.append(i.food_liked)
    context = {
        'liked_food': liked_food,
    }
    return render(request, 'user/user_detail.html', context)
