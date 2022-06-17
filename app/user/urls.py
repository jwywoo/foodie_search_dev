from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_create, name='user-create'),
    path('logout/', user_logout, name='logout'),
    path('postsignUp/', postsignUp, name='signup'),
]
