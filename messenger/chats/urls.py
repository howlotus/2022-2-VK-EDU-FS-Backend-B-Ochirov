"""This module defines urls of chats app"""

from django.urls import path
from .views import get_chats, add_chat, get_chat, update_chat, delete_chat

urlpatterns = [
    path('', get_chats, name='get_chats'),
    path('add_chat/', add_chat, name='add_chat'),
    path('get_chat/<int:chat_id>/', get_chat, name='get_chat'),
    path('update_chat/<int:chat_id>/', update_chat, name='update_chat'),
    path('delete_chat/<int:chat_id>/', delete_chat, name='delete_chat')
]
