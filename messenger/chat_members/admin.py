from django.contrib import admin
from .models import ChatMember


# Register your models here.
class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'datetime_added')
    list_filter = ('user_id', 'chat_id', 'datetime_added')


admin.site.register(ChatMember, ChatMemberAdmin)
