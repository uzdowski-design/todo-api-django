from rest_framework import serializers
from .models import Task, List


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(), source='parent.id')

    class Meta:
        model = Task
        fields = ('id', 'url', 'name', 'done', 'parent_id')

    def create(self, validated_data):
        subject = Task.objects.create(
            parent=validated_data['parent']['id'], name=validated_data['name'])

        return subject


class ListSerializer(serializers.HyperlinkedModelSerializer):
    children = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('id', 'url', 'name', 'children')
