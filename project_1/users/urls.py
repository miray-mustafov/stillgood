from django.urls import path, include

from project_1.users import views

urlpatterns = (
    path('register/', views.UserRegister.as_view(), name='user register'),
    path('login/', views.UserLogin.as_view(), name='user login'),
    path('logout/', views.UserLogout.as_view(), name='user logout'),

    path('<int:pk>/', include([
        path('', views.UserDetails.as_view(), name='user details'),
        path('edit/', views.UserEdit.as_view(), name='user edit'),
        path('delete/', views.UserDelete.as_view(), name='user delete'),
    ])),
)
