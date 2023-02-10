from django.db import models
from django.utils.translation import gettext as _

from ..users.models import User
from ..statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name=_('Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('Status'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Author'), related_name='author')
    executor = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name=_('Executor'),
                                 related_name='executor')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Date create'))
    tags = models.CharField(max_length=100, blank=True, verbose_name=_('Tags'))

    def __str__(self):
        return self.name
