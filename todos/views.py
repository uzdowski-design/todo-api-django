from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, List
from .serializers import TodoSerializer, ListSerializer


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListView(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
