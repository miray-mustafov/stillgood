from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from project_1.users.forms import UserRegisterForm, UserEditForm

# ACCOUNTS/VIEWS
UserModel = get_user_model()


class UserDetails(DetailView):
    context_object_name = 'current_user'
    template_name = 'users/user-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        return context


class UserEdit(UpdateView):
    context_object_name = 'current_user'
    template_name = 'users/user-edit.html'
    form_class = UserEditForm
    model = UserModel

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.object.pk})


class UserRegister(CreateView):
    template_name = 'users/user-register.html'
    success_url = reverse_lazy('user login')
    form_class = UserRegisterForm


class UserLogin(auth_views.LoginView):
    template_name = 'users/user-login.html'
    success_url = reverse_lazy('home page')


class UserLogout(auth_views.LogoutView):
    next_page = reverse_lazy('home page')


class UserDelete(DeleteView):
    #todo context_objname
    template_name = 'users/user-delete.html'
    model = UserModel
    success_url = reverse_lazy('home page')
