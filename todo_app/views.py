from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ['completed', 'priority', 'due_date', 'owner']
    search_fields = ['title']
    ordering_fields = ['created_at', 'due_date', 'title', 'priority']


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Task.objects.all()
            return Task.objects.filter(owner=user)
        return Task.objects.none()
    
    def perform_create(self, serializer):
        """Save the owner when a new task is created."""
        serializer.save(owner=self.request.user)


    

# View to retrieve, update, or delete a single task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_fields = ['completed', 'priority', 'due_date', 'owner']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'title', 'priority']

    def get_queryset(self):
        """
        should return a list of all tasks for the currently auth. user
        """
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(owner=user)
        return Task.objects.none() #empty queryset for unauthenticated users
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    