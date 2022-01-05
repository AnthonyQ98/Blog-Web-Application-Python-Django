from django.db import models
from django.db.models.fields.related import ForeignKey


class Article(models.Model):
    author = ForeignKey('auth.User', on_delete = models.CASCADE,)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    def __str__(self):
        return self.title

# Create your models here.
