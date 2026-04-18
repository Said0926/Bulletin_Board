from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at') # какие поля показывть
    search_fields = ('title',) # поиск по полям