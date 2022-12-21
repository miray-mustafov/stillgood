from django.contrib.auth.decorators import login_required
from django.urls import path
from project_1.common import views

urlpatterns = (
    path('', views.home_page, name='home page'),
    path('genres/', views.show_genres, name='genres'),
    path('category/<int:pk>/<str:title>/', views.list_filtered_items, name='list filtered items'),
    path('favourites/', login_required(views.list_favourite_items), name='list favourite items'),
    path('favourite/add/<int:item_pk>/', login_required(views.add_a_favourite), name='add a favourite'),
)
