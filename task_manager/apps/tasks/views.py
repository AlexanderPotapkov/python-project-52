from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, DetailView
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django_filters.views import FilterView

from .models import Task
from .utils import DataMixin
from .filters import TaskFilter


class TasksView(DataMixin, FilterView):
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'


class ShowTask(DataMixin, DetailView):
    template_name = 'tasks/task_view.html'
    context_object_name = 'task'


class CreateTask(DataMixin, CreateView):
    extra_context = {'header': _('Create task'),
                     'button': _('Create')}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, _('The task created successfully'))
        return super(CreateTask, self).form_valid(form)


class UpdateTask(DataMixin, UpdateView):
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_message = _('The task changed successfully')
    extra_context = {'header': _('Change task'),
                     'button': _('Change')}


class DeleteTask(DataMixin, UserPassesTestMixin, DeleteView):
    model = Task
    login_url = 'login'
    success_url = reverse_lazy('tasks')
    template_name = 'crud/delete.html'
    success_message = _('The task deleted successfully')
    extra_context = {'title': _('Delete task')}

    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = _('The task can only be deleted by its author')
            url = reverse_lazy('tasks')
        else:
            message = _('You need to authenticated')
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)
