from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name=_('Name'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Name')
        verbose_name_plural = _('Names')
        ordering = ['date_created', ]
