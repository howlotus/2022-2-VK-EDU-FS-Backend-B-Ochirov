"""This module defines urls of users app"""

from django.urls import path
from .views import get_users, add_user, get_user, update_user, delete_user

urlpatterns = [
    path('', get_users, name='get_users'),
    path('add_user/', add_user, name='add_user'),
    path('get_user/<int:user_id>/', get_user, name='get_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user')
]
