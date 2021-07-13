from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Contact(models.Model):
    message_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username+" message."