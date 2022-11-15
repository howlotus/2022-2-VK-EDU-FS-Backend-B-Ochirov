from django.contrib import admin
from .models import Chat, ChatMember


# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'datetime_created')
    list_filter = ('datetime_created', )


class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'datetime_added')
    list_filter = ('user_id', 'chat_id', 'datetime_added')


admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMember, ChatMemberAdmin)
