from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(List, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
