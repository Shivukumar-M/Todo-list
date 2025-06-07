from django.db import models


# class Task(models.Model):
#     progress = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Progress: {self.progress}%"
    
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    todo_date=models.DateField(auto_now=True)
    # task = models.OneToOneField(Task, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

