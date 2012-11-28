from django.contrib import admin
from models import Game, Item

class GameAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_time')
    list_filter = ['created_time']
    date_hierarchy = 'created_time'
    list_select_related = True
    
admin.site.register(Game, GameAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('game', 'picture', 'picture_width', 'picture_height', 'created_time')

admin.site.register(Item, ItemAdmin)