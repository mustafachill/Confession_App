from django.contrib.auth.models import User
from django.db import models

class Confession(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=250)
    likes = models.ManyToManyField(User, related_name='liked_confessions', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_confessions', blank=True)

    def __str__(self):
        return f"Confession owner's username: {self.username}, owner's message: {self.message}"