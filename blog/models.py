from django.db import models
from datetime import datetime


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    posted = models.DateTimeField(default=datetime.now, blank=True) # auto_now_add=True