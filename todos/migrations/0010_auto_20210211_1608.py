# Generated by Django 3.1.6 on 2021-02-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_auto_20210211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
