from django.urls import path
from project_1.common import views

urlpatterns = (
    path('', views.home_page, name='home page'),
)
