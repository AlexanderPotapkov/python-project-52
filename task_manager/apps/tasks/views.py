from django.views.generic import ListView, CreateView, UpdateView
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Task
from .utils import DataMixin


class TasksView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'


class CreateTask(DataMixin, CreateView):
    extra_context = {'header': _('Create task'),
                     'button': _('Create')}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, _('Task created successfully'))
        return super(CreateTask, self).form_valid(form)


class UpdateTask(DataMixin, UpdateView):
    success_message = _('Task changed successfully')
    extra_context = {'header': _('Change task'),
                     'button': _('Change')}
