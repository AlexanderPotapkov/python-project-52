from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name=_('Name'))
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.name
