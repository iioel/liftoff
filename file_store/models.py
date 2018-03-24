import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=300)
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = "file"
        ordering = ['date']

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)

    class Meta:
        verbose_name = "tag"
        ordering = ['name']
