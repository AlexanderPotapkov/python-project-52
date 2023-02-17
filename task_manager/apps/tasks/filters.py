from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.utils.translation import gettext as _
from django import forms

from .models import Task
from ..statuses.models import Status
from ..users.models import User
from ..labels.models import Label


class TaskFilter(FilterSet):

    def my_task_filter(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user', None)
            queryset = queryset.filter(author=author)
        return queryset

    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label=_('Status'),
                               widget=forms.Select(
                                   attrs={'name': 'status',
                                          'class': 'custom-select d-block',
                                          'title_id': 'id_status'}))

    executor = ModelChoiceFilter(queryset=User.objects.all(),
                                 label=_('Executor'),
                                 widget=forms.Select(
                                     attrs={'name': 'executor',
                                            'class': 'custom-select d-block',
                                            'title_id': 'id_executor'}))

    labels = ModelChoiceFilter(queryset=Label.objects.all(),
                              label=_('Label'),
                              widget=forms.Select(
                                  attrs={'name': 'label',
                                         'class': 'custom-select d-block',
                                         'title_id': 'id_label'}))

    self_task = BooleanFilter(label=_('Only your tasks'),
                              widget=forms.widgets.CheckboxInput(
                                  attrs={'name': 'self_tasks',
                                         'title_id': 'id_self_tasks'}),
                              method='my_task_filter',
                              )


class Meta:
    model = Task
    fields = ['status', 'executor', 'labels', 'self_task']
