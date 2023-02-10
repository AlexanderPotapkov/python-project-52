from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name=_('Name'))
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')

    def __str__(self):
        return self.name
