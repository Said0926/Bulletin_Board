from django.contrib import admin
from .models import Bulletin, Response

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'category', 'created_at') # какие поля показывать
    search_fields = ('title', 'author__email') # поиск по каким полям
    list_filter   = ('category',)  # фильтр  по категориям


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display  = ('author', 'bulletin', 'is_accepted', 'created_at') #какие поля показывать
    search_fields = ('author__email',) #поиск по каким полям
    list_filter   = ('is_accepted',) #фильтр  по принятым
    
