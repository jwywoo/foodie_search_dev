from django.urls import path

from .views import main, searching_foods

app_name = 'food'
urlpatterns = [
    path('', main, name='main'),
    path('search/', searching_foods, name='searching-food')
]