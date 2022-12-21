from django.contrib.auth.decorators import login_required
from django.urls import path, include
from project_1.items import views


urlpatterns = (
    # path('add/', login_required(views.ItemAddView.as_view()), name='item add'),
    path('add/', login_required(views.item_add_view), name='item add'),

    path('<int:pk>/', include([
        path('', views.ItemDetails.as_view(), name='item details'),
        path('edit/', login_required(views.ItemEditView.as_view()), name='item edit'),
        path('delete/', login_required(views.ItemDelete.as_view()), name='item delete'),
    ])),
)
