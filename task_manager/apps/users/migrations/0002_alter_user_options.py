# Generated by Django 4.1.5 on 2023-01-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
