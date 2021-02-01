from rest_framework import serializers
from .models import Todo, List


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'url', 'name', 'done')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'url', 'name', 'tasks')
