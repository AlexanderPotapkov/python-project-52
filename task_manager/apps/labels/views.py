from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError

from .models import Label
from .utils import DataMixin


class LabelsView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/labels.html'


class CreateLabel(DataMixin, CreateView):
    success_message = _('Label created successfully')
    extra_context = {'header': _('Create label'),
                     'button': _('Create')}


class UpdateLabel(DataMixin, UpdateView):
    success_message = _('Label changed successfully')
    extra_context = {'header': _('Change label'),
                     'button': _('Change')}


class DeleteLabel(DataMixin, DeleteView):
    model = Label
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Delete label'),
    }

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request,
                             _('Label deleted successfully'))
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             _('Unable to delete label, because it is used'))
            return redirect(success_url)
