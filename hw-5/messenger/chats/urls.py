"""This module defines urls of chats app"""

from django.urls import path
from .views import default_chat_handler, rud_chat_handler

urlpatterns = [
    path('', default_chat_handler, name='list_or_create_handler'),
    path('<int:chat_id>/', rud_chat_handler, name='edit_chat_handler')
]
