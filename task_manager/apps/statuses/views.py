from django.views.generic import ListView

from .models import Statuses


class StatusesView(ListView):
    model = Statuses
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'
