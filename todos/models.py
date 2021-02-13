from django.db import models


# List model, list only has a name set up by the model and another link (children) created and linked in serializers (plus automatic fields - id, url)
class List(models.Model):
    name = models.CharField(max_length=50)

    # method to return model name
    def __str__(self):
        return self.name


# Task model requires name, done status (defaulted to false), parent (list under which it was created), and due date (defaulted to null, but can be set up bu user on front end if needed)
class Task(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    parent = models.ForeignKey(
        List, related_name='children', on_delete=models.CASCADE)  # this creates link to parent (list) and deletes item if parent is deleted (no orphan tasks)
    due_date = models.DateField(null=True, default=None)

    # method to return object name
    def __str__(self):
        return self.name
