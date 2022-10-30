"""This module defines urls of chats app"""

from django.urls import path
from .views import chat_menu, get_chat_list, create_chat_handler, edit_chat_handler

urlpatterns = [
    path('', chat_menu, name='chat_menu'),
    path('list/', get_chat_list, name='get_chat_list'),
    path('create/', create_chat_handler, name='create_chat_handler'),
    path('<int:chat_id>/', edit_chat_handler, name='edit_chat_handler')
]
