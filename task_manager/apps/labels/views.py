from django.views.generic import ListView, CreateView
from django.utils.translation import gettext as _

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
