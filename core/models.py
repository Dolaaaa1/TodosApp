from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.TextField(max_length=500)
    
    
    
    
    def __str__(self):
        return self.text
