"""This module defines urls of messages app"""

from django.urls import path
from .views import create_message_handler, edit_message_handler

urlpatterns = [
    path('create/<int:chat_id>/', create_message_handler, name='create_message_handler'),
    path('<int:message_id>/', edit_message_handler, name='edit_message_handler')
]