from rest_framework import serializers
from .models import Task, List


# Task Serializer, creates the representation of Task data sent (json) from DB to front end on api call
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # parent id is needed to link task to the list under which it was created
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(), source='parent.id')
    # Meta class defines the fields that need to be presented on api call

    class Meta:
        model = Task
        fields = ('id', 'url', 'name', 'done', 'parent_id', 'due_date')
    # This method creates a parent-child link

    def create(self, validated_data):
        subject = Task.objects.create(
            parent=validated_data['parent']['id'], name=validated_data['name'])

        return subject


# List Serializer creates the reprezentation of List data sent (json) from DB to front end on API call
class ListSerializer(serializers.HyperlinkedModelSerializer):
    # children is an array of objects in List item that represents all Tasks that are linked to this list.
    children = TaskSerializer(many=True, read_only=True)

    # Meta class defines the fields that need to be presented on api call
    class Meta:
        model = List
        fields = ('id', 'url', 'name', 'children')
