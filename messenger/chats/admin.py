from django.contrib import admin
from .models import Chat


# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'datetime_created')
    list_filter = ('datetime_created', )


admin.site.register(Chat, ChatAdmin)
