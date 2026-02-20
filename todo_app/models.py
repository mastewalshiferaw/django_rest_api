from django.db import models

class Task(models.Model):
    PRIORITY_CHOICE = [
        ('L', 'Low'),
        ('M', 'Middle'),
        ('H', 'High')

    ]
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    priority=models.CharField(max_length=1, choices=PRIORITY_CHOICE, blank=True, null=True, help_text="Task Priority (Low, Medium, High)")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['created_at']


