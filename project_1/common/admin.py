from django.contrib import admin
from project_1.common.models import Favourite


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'user')
