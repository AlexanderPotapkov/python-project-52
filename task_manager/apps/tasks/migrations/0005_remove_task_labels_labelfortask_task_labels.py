# Generated by Django 4.1.6 on 2023-02-10 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_remove_task_tags_task_labels_alter_task_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='labels',
        ),
        migrations.CreateModel(
            name='LabelForTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='labels.label')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.LabelForTask', to='labels.label', verbose_name='Метки'),
        ),
    ]
