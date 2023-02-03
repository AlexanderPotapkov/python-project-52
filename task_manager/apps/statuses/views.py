from django.views.generic import ListView


class StatusesView(ListView):
    template_name = 'statuses/statuses.html'
