# Generated by Django 3.1.6 on 2021-02-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=None),
        ),
    ]