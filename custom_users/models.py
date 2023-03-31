from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(max_length=150, null=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    birthday = models.DateField(blank=True, null=True)
    imageUrl = models.TextField(null=True) 
    created_by = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email