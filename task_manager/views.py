from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'task_manager/index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'task_manager/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
