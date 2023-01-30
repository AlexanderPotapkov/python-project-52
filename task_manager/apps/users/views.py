from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _

from task_manager.apps.users.forms import RegisterUserForm


class UsersView(TemplateView):
    template_name = 'users/users.html'


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
