# Generated by Django 4.1.6 on 2023-02-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_alter_statuses_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuses',
            options={'ordering': ['date_created'], 'verbose_name': 'Имя', 'verbose_name_plural': 'Имена'},
        ),
    ]