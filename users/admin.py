from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'sport', 'is_staff', 'is_active')
    list_filter = ('role', 'sport', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'sport')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Role Info', {'fields': ('role', 'sport')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'sport', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
