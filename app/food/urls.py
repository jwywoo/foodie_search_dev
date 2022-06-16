from django.urls import path

# from .views import main, searching_foods, food_detail
from . import views
app_name = 'food'
urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.searching_foods, name='searching-food'),
    path('<int:pk>/', views.food_detail, name='food-detail'),
    path('<int:pk>/', views.user_add_favorite, name='add_favorite'),
    path('<int:pk>/', views.user_removing_favorite, name='remove_favorite'),
]