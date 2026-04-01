from rest_framework import serializers
from .models import Task,  SubTask
from django.contrib.auth.models import User
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)

        model =User
        fields = ('id', 'username', 'email', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }


class TaskSerializer(serializers.ModelSerializer):
    subtasks=SubTaskSerializer(many=True,)
    owner = UserSerializer(read_only=True)
    #makes owner field nested and read only
    class Meta:
        
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'due_date', 'priority', 'owner']
        
        extra_kwargs = {
            'priority': {'read_only': True},
            'created_at': {'read_only': True}
        }
    
    def validate_due_date(self, value):
        if value and value < timezone.now.date():
            raise serializers.ValidationError("Due date cannot be in the past!")
        
        return value
    
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'completed']


class TaskSerializer(serializers.ModelSerializer):
    # This automatically includes subtasks when you GET a task
    subtasks = SubTaskSerializer(many=True, required=False) 
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'due_date', 'priority', 'owner', 'subtasks']

        def create(self, validated_data):
        # EVERYTHING below must be indented by 4 spaces
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)
        
        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)
        
        return task