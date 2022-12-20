from django.shortcuts import render

from project_1.common.models import Category
from project_1.items.models import Item
from django.core.paginator import Paginator, EmptyPage


def home_page(request):
    items_recent = Item.objects.all().order_by('-date_added')[:18]
    paginator = Paginator(items_recent, 9)
    page = request.GET.get('page')
    page_items_recent = paginator.get_page(page)

    context = {
        'items_recent': page_items_recent,
        # 'is_owner': request.user ==
    }
    return render(request, template_name='common/home-page.html', context=context)


def show_genres(request):

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template_name='genres.html', context=context)
