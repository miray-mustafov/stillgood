from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from project_1.items.models import Item, ItemImage, Category


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 5


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_new', 'get_image', 'date_added')
    list_display_links = ('id', 'title',)
    list_filter = ('category', 'is_new', 'phone',)
    search_fields = ('title', 'location',)
    search_help_text = 'Search by title and location'
    list_editable = ('is_new',)
    list_per_page = 15
    inlines = [ItemImageInline]


@admin.register(ItemImage)
class MultipleImageAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('id', 'title', 'parent',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    search_help_text = 'search by category title'
