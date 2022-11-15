from django.contrib import admin
from .models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'sender_id', 'content', 'datetime_sent', 'status')
    list_filter = ('chat_id', 'sender_id', 'datetime_sent', 'status')


admin.site.register(Message, MessageAdmin)
