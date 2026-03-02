from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ['completed', 'priority', 'due_date', 'owner']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'title', 'priority']

     def perform_create(self, serializer):
        """Save the owner when a new task is created."""
        serializer.save(owner=self.request.user)
# View to retrieve, update, or delete a single task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer