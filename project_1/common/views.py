from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from project_1.common.forms import SearchForm
from project_1.common.models import Favourite
from project_1.items.models import Category, Item
from django.core.paginator import Paginator, EmptyPage

ITEMS_COUNT_PER_PAGE = 5
ITEMS_RECENT_TO_SHOW = 50


def home_page(request):
    items_recent = Item.objects.all().order_by('-date_added')[:ITEMS_RECENT_TO_SHOW]
    categories = Category.objects.all()

    p = Paginator(items_recent, ITEMS_COUNT_PER_PAGE)
    page_num = request.GET.get('page', default=1)
    try:
        page_items = p.page(page_num)
    except EmptyPage:
        page_items = p.page(1)

    context = {
        'categories': categories,
        'items': page_items,
        'where': 'in all items',
    }
    return render(request, template_name='common/home-page.html', context=context)


def list_categorized_items(request, pk, title):
    categories = Category.objects.all()
    items_categorized = Item.objects.filter(category_id=pk)

    if request.user.is_authenticated:
        favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
    else:
        favourite_items_by_requser = []

    context = {
        'categories': categories,
        'items': items_categorized,
        'category_title': title,
        'favourite_items_by_requser': favourite_items_by_requser,
    }
    return render(request, template_name='common/list-categorized-items.html', context=context)


def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            categ_id = search_form.cleaned_data['categ_id']
            where = 'in the website'
            categories = Category.objects.all()
            search_query = f'"{query}"'

            if query == '@' and categ_id == 0: # '@' signals the case where search input was left blank, so we filter by category only
                return HttpResponseRedirect('/')
            elif query == '@':
                search_query = ''
                where = f'{categories.get(pk=categ_id).title} category'
                searched_items = Item.objects.filter(category__id=categ_id)
            elif categ_id == 0:
                searched_items = Item.objects.filter(title__icontains=query)
            else:
                where = f'in {categories.get(pk=categ_id).title} category'
                searched_items = Item.objects.filter(title__icontains=query, category__id=categ_id)

            if request.user.is_authenticated:
                favourite_items_by_requser = [f.item_id for f in request.user.favourite_set.all()]
            else:
                favourite_items_by_requser = []

            context = {
                'categories': categories,
                'items': searched_items,
                'favourite_items_by_requser': favourite_items_by_requser,
                'query': f'{search_query}',
                'where': where,
            }
            return render(request, template_name='common/list-searched-items.html', context=context)

    return HttpResponseRedirect('/')


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


def list_favourite_items(request, username):
    categories = Category.objects.all()
    favourite_items = [f.item for f in request.user.favourite_set.all()]

    context = {
        'categories': categories,
        'items': favourite_items,
    }

    return render(request, template_name='common/list-favourite-items.html', context=context)

# def paginate(request, items):
#     p = Paginator(items, ITEMS_COUNT_PER_PAGE)
#     page_num = request.GET.get('page', default=1)
#     try:
#         page_items = p.page(page_num)
#     except EmptyPage:
#         page_items = p.page(1)
#
#     return page_items
