"""This module defines urls of chats app"""

from django.urls import path
from .views import chat_menu, chat_list, add_chat, chat_detail

urlpatterns = [
    path('', chat_menu, name='chat_menu'),
    path('list/', chat_list, name='chat_list'),
    path('add/', add_chat, name='add_chat'),
    path('<int:chat_id>/', chat_detail, name='chat_detail')
]
