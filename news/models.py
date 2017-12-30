from django.db import models
     

class Article(models.Model):
    title = models.CharField(max_length=1000)
    shortcut = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

