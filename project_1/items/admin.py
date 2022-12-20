from django.contrib import admin

from project_1.items.models import Item, ItemImage


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 5


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_new', 'get_image')
    list_labels = {
        'id': 'idd'
    }
    list_display_links = ('id', 'title',)
    list_filter = ('category', 'is_new', 'phone')
    search_fields = ('title', 'location',)
    search_help_text = 'Search by title and location'
    list_editable = ('is_new',)
    list_per_page = 15
    inlines = [ItemImageInline]


@admin.register(ItemImage)
class MultipleImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
