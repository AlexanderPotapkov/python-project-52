from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'task_manager/index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'task_manager/authentication.html'
    success_message = _("You were logged in")


class LogoutUser(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("You were logged out"))
        return super().dispatch(request, *args, **kwargs)
