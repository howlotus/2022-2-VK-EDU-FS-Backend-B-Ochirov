"""This module defines urls of messages app"""

from django.urls import path
from .views import default_message_handler, rud_message_handler

urlpatterns = [
    path('', default_message_handler, name='create_message_handler'),
    path('<int:message_id>/', rud_message_handler, name='edit_message_handler')
]
