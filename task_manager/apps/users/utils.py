from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect


class DataMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = _('You do not have rights to change another user')
            url = reverse_lazy('users')
        else:
            message = _('You are not authorized! Please sign in')
            url = reverse_lazy('login')
        messages.warning(self.request, message)
        return redirect(url)
