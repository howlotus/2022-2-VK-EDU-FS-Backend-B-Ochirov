"""This module defines urls of messages app"""

from django.urls import path
from .views import get_messages, add_message, get_message, make_message_checked, update_message, delete_message

urlpatterns = [
    path('', get_messages, name='get_messages'),
    path('add_message/', add_message, name='add_message'),
    path('get_message/<int:message_id>/', get_message, name='get_message'),
    path('check_message/<int:message_id>/', make_message_checked, name='make_message_checked'),
    path('update_message/<int:message_id>/', update_message, name='update_message'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message')
]
