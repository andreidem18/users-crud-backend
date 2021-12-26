from django.db import models
from users.models import User

class Phone(models.Model):
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='phones')

    def __str__(self):
        return self.phone
    