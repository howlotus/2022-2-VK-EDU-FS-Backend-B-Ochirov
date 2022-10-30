"""This module defines urls of users app"""

from django.urls import path
from .views import default_user_handler, rud_user_handler

urlpatterns = [
    path('', default_user_handler, name='default_user_handler'),
    path('<int:user_id>/', rud_user_handler, name='rud_user_handler')
]
