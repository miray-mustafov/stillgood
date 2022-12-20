from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin

from project_1.users.forms import UserEditForm, UserRegisterForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserRegisterForm
    list_display = ("username", 'id', "email", "first_name", "last_name", "is_staff", 'img')
    search_fields = ('user',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'personal_photo',
                    'first_name',
                    'last_name',
                    'gender',
                    'phone',
                    'location',
                    'email',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )
