from django.db import models
from Users.models import User
from Tasks.models import Task
from Project.models import Project


# Create your models here.
class Notificaton(models.Model):

    NOTIFICATION_TYPES= [
        ('TASK_ASSIGNED','Task Assigned'),
        ('TASK_STATUS_CHANGED','Task Status Changed' ),
        ('PROJECT_UPDATED', 'Project Updated'),
    ]

    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification= models.CharField(max_length=20, choices= NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message= models.TextField()
    related_task= models.ForeignKey(Task, on_delete= models.SET_NULL, null= True, blank= True)
    related_project= models.ForeignKey(Project, on_delete= models.SET_NULL , null = True, blank= True)
    is_read= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return self.title
