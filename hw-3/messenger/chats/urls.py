from django.urls import path

from chats.views import chat_list, add_chat, chat_detail

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('add/', add_chat, name='add_chat'),
    path('<int:chat_id>/', chat_detail, name='chat_detail')
]
