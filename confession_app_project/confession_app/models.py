from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Confession(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"Confession owner's username: {self.username}, owner's message: {self.message}"
    
    