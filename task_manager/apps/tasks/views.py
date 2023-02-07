from django.views.generic import ListView

from .models import Task


class TasksView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'
