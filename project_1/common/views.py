from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from project_1.common.forms import SearchForm
from project_1.common.models import Favourite
from project_1.items.models import Category, Item
from django.core.paginator import Paginator, EmptyPage


def home_page(request):
    items_recent = Item.objects.all().order_by('-date_added')[:18]
    categories = Category.objects.all()
    paginator = Paginator(items_recent, 9)
    page = request.GET.get('page')
    page_items_recent = paginator.get_page(page)

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            searched_items = Item.objects.filter(title__icontains=query)
            categories = Category.objects.all()

            if request.user.is_authenticated:
                favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
            else:
                favourite_items_by_requser = []

            context = {
                'search_form': search_form,
                'categories': categories,
                'searched_items': searched_items,
                'favourite_items_by_requser': favourite_items_by_requser,
                'query': query,
            }
            return render(request, template_name='common/list-searched-items.html', context=context)

    context = {
        'search_form': SearchForm(),
        'categories': categories,
        'items_recent': page_items_recent,
        # 'is_owner': request.user ==
    }
    return render(request, template_name='common/home-page.html', context=context)


# todo change to list_categorized
def list_categorized_items(request, pk, title):
    categories = Category.objects.all()
    items_categorized = Item.objects.filter(category_id=pk)

    if request.user.is_authenticated:
        favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
    else:
        favourite_items_by_requser = []

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            searched_items = items_categorized.filter(title__icontains=query)
            categories = Category.objects.all()

            if request.user.is_authenticated:
                favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
            else:
                favourite_items_by_requser = []

            context = {
                'search_form': search_form,
                'categories': categories,
                'searched_items': searched_items,
                'favourite_items_by_requser': favourite_items_by_requser,
                'query': query,
            }
            return render(request, template_name='common/list-searched-items.html', context=context)

    context = {
        'search_form': SearchForm(),
        'categories': categories,
        'items_categorized': items_categorized,
        'category_title': title,
        'favourite_items_by_requser': favourite_items_by_requser,
    }
    return render(request, template_name='common/list-categorized-items.html', context=context)

def add_a_favourite(request, item_pk):
    # with login_required works improperly
    if not request.user.is_authenticated:
        return redirect('user login')

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

    # todo: create partial template for hearts
    favourite_items = [f.item for f in request.user.favourite_set.all()]
    context = {
        'categories': categories,
        'favourite_items': favourite_items,
    }

    return render(request, template_name='common/favourites.html', context=context)
