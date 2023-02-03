from django.views.generic import ListView

from .models import Statuses


class StatusesView(ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
