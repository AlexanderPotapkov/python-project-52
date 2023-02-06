from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError

from .models import Statuses


class StatusesView(ListView):
    model = Statuses
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Statuses
    fields = ['name']
    template_name = 'crud/create_and_update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status is successfully created')
    extra_context = {'header': _('Create status'),
                     'button': _('Create')}


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    fields = ['name']
    template_name = 'crud/create_and_update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status is successfully changed')
    extra_context = {'header': _('Change status'),
                     'button': _('Change')}


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
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
                             _('The status is successfully deleted'))
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             _('Unable to delete status, because it is used'))
            return redirect(success_url)
