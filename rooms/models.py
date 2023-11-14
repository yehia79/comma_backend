from django.db import models
from branches.models import Branch  
from users.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch , on_delete=models.CASCADE, related_name='branch', default=None)

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client= models.ForeignKey(User, on_delete=models.CASCADE, related_name='client', default=None)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    
