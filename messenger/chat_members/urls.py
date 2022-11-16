"""This module defines urls of members app"""

from django.urls import path
from .views import add_member, delete_member

urlpatterns = [
    path('add_member/', add_member, name='add_member'),
    path('delete_member/', delete_member, name='delete_member')
]
