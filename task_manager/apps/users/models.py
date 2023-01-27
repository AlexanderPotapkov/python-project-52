from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class User(AbstractUser):

    def __str__(self):
        return self.get_full_name()

    # def get_absolute_url(self):
    #     return reverse('users', kwargs={'id_username': self.pk})

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['date_joined',]
