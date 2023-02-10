from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from .models import Task


class DataMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    fields = '__all__'
    template_name = 'crud/create_and_update.html'
    success_url = reverse_lazy('tasks')
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, _('You need to authenticated'))
        return redirect(self.login_url)
