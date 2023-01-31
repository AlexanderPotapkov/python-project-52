from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

from task_manager.apps.users.forms import RegisterUserForm
from .models import User


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users.html'


class RegisterUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'header': _('Registration'),
                     'button': _('Register')}


class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users')
    extra_context = {'header': _('Update user'),
                     'button': _('Update')}

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = _('You do not have rights to change another user.')
            url = reverse_lazy('users')
        else:
            message = _('You are not authorized! Please sign in.')
            url = reverse_lazy('login')
        messages.warning(self.request, message)
        return redirect(url)
