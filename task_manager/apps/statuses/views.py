from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError

from .models import Status
from .utils import DataMixin


class StatusesView(ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'


class CreateStatus(DataMixin, CreateView):
    success_message = _('Status created successfully')
    extra_context = {'header': _('Create status'),
                     'button': _('Create')}


class UpdateStatus(DataMixin, UpdateView):
    success_message = _('Status changed successfully')
    extra_context = {'header': _('Change status'),
                     'button': _('Change')}


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('statuses')
    extra_context = {
        'title': _('Delete status'),
    }

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request,
                             _('Status deleted successfully'))
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             _('Unable to delete status, because it is used'))
            return redirect(success_url)
