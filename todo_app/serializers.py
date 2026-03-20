from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)

        model =User
        fields = ('id', 'username', 'email', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    #makes owner field nested and read only
    class Meta:
        
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'due_date', 'priority', 'owner']
        
        extra_kwargs = {
            'priority': {'read_only': True},
            'created_at': {'read_only': True}
        }