from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'phone')
    filter_horizontal = ()
    list_filter = ('is_superuser', 'is_active')
    fieldsets = ()
    list_display_links = ['phone']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileAdmin)
