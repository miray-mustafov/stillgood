from django.contrib import admin

from project_1.items.models import Item, ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_new',)
    list_display_links = ('id', 'title',)
    list_filter = ('category', 'is_new', 'phone')
    search_fields = ('title', 'location',)
    list_editable = ('is_new',)
    list_per_page = 15


@admin.register(ItemImage)
class MultipleImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
