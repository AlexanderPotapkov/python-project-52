from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = 'task_manager/index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'task_manager/login.html'
    success_message = _('You have successfully logged in')


class LogoutUser(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _('You have successfully logged out'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')
