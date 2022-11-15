from django.contrib import admin
from .models import User, UserProfile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'username', 'date_joined')
    list_filter = ('date_joined', )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'info', 'user_id')
    list_filter = ('full_name', )


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
