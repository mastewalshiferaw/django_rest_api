from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True) # New field!
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        blank=True,
        null=True,
        help_text="Task priority (Low, Medium, High)"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']



class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

