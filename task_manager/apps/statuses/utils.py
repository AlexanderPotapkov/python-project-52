from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Statuses


class DataMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Statuses
    fields = ['name']
    template_name = 'crud/create_and_update.html'
    success_url = reverse_lazy('statuses')
