from django.shortcuts import render, redirect

from project_1.common.models import Favourite
from project_1.items.models import Category, Item
from django.core.paginator import Paginator, EmptyPage


def home_page(request):
    items_recent = Item.objects.all().order_by('-date_added')[:18]

    paginator = Paginator(items_recent, 9)
    page = request.GET.get('page')
    page_items_recent = paginator.get_page(page)

    categories = Category.objects.all()

    context = {
        'items_recent': page_items_recent,
        'categories': categories,
        # 'is_owner': request.user ==
    }
    return render(request, template_name='common/home-page.html', context=context)


def list_filtered_items(request, pk, title):
    categories = Category.objects.all()

    items_filtered = Item.objects.filter(category_id=pk)

    if request.user.is_authenticated:
        favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
    else:
        favourite_items_by_requser = []

    context = {
        'categories': categories,
        'items_filtered': items_filtered,
        'category_title': title,
        'favourite_items_by_requser': favourite_items_by_requser,
    }
    return render(request, template_name='common/list_filtered_items.html', context=context)


def add_a_favourite(request, item_pk):
    favoured_item = Favourite.objects.filter(item_id=item_pk, user=request.user).first()

    if favoured_item:
        favoured_item.delete()
    else:
        Favourite.objects.create(
            item_id=item_pk,
            user=request.user
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{item_pk}')


def list_favourite_items(request):
    categories = Category.objects.all()

    favourite_items = [f.item for f in request.user.favourite_set.all()]
    context = {
        'categories': categories,
        'favourite_items': favourite_items,
    }

    return render(request, template_name='common/favourites.html', context=context)


def show_genres(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template_name='genres.html', context=context)
