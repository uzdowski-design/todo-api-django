from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, List
from .serializers import TaskSerializer, ListSerializer


# Create Task View (api representation)
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Create List View (api representation)
class ListView(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
