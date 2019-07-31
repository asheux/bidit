from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    list_filter = ('is_superuser',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)

