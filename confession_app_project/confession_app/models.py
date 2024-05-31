from django.db import models

# Create your models here.

class Confession(models.Model):
    nickname = models.CharField(max_length=50)
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"Confession owner's nickname: {self.nickname}, owner's message: {self.message}"
    
    