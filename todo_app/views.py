from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    