from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    parent = models.ForeignKey(
        List, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
