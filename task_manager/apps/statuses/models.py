from django.db import models
from django.utils.translation import gettext as _


class Statuses(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Name')
        verbose_name_plural = _('Names')
        ordering = ['date_created', ]

    def __str__(self):
        return self.name
