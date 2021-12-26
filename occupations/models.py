from django.db import models

class Occupation(models.Model):
    occupation = models.CharField(max_length=30)
    
    def __str__(self):
        return self.occupation
