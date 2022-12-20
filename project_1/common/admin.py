from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from project_1.common.models import Category
from project_1.items.models import Item


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('id', 'title', 'parent')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    search_help_text = 'search by category title'








    # Main administration for category but:
    # Unsupported lookup 'lft' for CharField or join on the field not permitted, perhaps you meant lt or lte?
    #
    # mptt_indent_field = "title"
    # list_display = ('tree_actions', 'indented_title',
    #                 'related_products_count', 'related_products_cumulative_count')
    # list_display_links = ('indented_title',)
    #
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #
    #     # Add cumulative product count
    #     qs = Category.objects.add_related_count(
    #         qs,
    #         Item,
    #         'category',
    #         'products_cumulative_count',
    #         cumulative=True)
    #
    #     # Add non cumulative product count
    #     qs = Category.objects.add_related_count(
    #         qs,
    #         Item,
    #         'category',
    #         'products_count',
    #         cumulative=False)
    #     return qs
    #
    # def related_products_count(self, instance):
    #     return instance.products_count
    #
    # related_products_count.short_description = 'Related products (for this specific category)'
    #
    # def related_products_cumulative_count(self, instance):
    #     return instance.products_cumulative_count
    #
    # related_products_cumulative_count.short_description = 'Related products (in tree)'
