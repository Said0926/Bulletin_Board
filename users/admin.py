from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # какие колонки видно в списке пользователей
    list_display = ('email', 'is_confirmed', 'is_subscribed_to_newsletter', 'is_staff')
    
    # по каким полям можно искать
    search_fields = ('email',)
    
    # убираем username из форм так как мы его удалили
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Права', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Доп. инфо', {'fields': ('is_confirmed', 'is_subscribed_to_newsletter')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)