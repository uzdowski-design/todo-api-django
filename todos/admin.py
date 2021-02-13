from django.contrib import admin
from .models import Task, List

# making Task and List modules available in the admin panel
admin.site.register(Task)
admin.site.register(List)
