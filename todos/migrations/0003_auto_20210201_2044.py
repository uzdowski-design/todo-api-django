# Generated by Django 3.1.6 on 2021-02-01 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='todos',
            new_name='tasks',
        ),
    ]
