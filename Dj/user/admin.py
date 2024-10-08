from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class Admin(UserAdmin):
    list_display = ('phone', 'email', 'is_active', 'pk',)
    filter_horizontal = ()
    list_filter = ('is_active',)
    fieldsets = ()
    search_fields = ('email', 'phone')
    list_display_links = ('phone', 'email')


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'email', 'pk']
    search_fields = ('phone', 'user')
    sortable_by = ('pk', 'user')


admin.site.register(User, Admin)

admin.site.register(Profile, AdminProfile)
