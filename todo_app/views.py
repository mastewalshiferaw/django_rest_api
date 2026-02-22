from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

#a view to list all tasks and create new tasks
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

   

#View to retrieve, update, or delete a single task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    filterset_fields = ['completed', 'priority', 'due_date']

    search_fields = ['title', 'description']

    ordering_fields = ['created_at', 'due_date', 'title', 'priority']

# View to retrieve, update, or delete a single task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer