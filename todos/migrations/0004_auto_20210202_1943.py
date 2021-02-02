# Generated by Django 3.1.6 on 2021-02-02 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20210201_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='tasks',
        ),
        migrations.AddField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.list'),
        ),
    ]