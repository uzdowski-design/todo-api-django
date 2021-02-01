from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Todo)

    def __str__(self):
        return self.name
