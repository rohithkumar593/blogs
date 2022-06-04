from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title=models.CharField(max_length=65535)
    author=models.CharField(max_length=65535)
    body=models.CharField(max_length=65535)
    admin_approved=models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.title)+" "+str(self.author)

# Create your models here.


