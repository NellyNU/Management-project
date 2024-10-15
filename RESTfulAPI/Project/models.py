from django.db import models
from Users.models import User

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES= [
        ('NEW','New'),
        ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW') 
    manager= models.ForeignKey(User,  on_delete= models.SET_NULL,null=True,related_name="managed_projects")
    team_members = models.ManyToManyField(User, related_name="projects" )

    def __str__(self):
        return self.name