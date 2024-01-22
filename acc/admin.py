# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('email',)
    list_display = ('email', 'name', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('name',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

