from django.db import models


class Statuses(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
