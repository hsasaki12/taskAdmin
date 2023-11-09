from django.db import models
from pathlib import Path


def upload_image_to(instance, filename):
    return Path('static') / 'images' / filename


class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()
    duedate = models.DateField()
    image = models.ImageField(
        default=None, blank=True, null=True, upload_to=upload_image_to)

    def __str__(self):
        return self.title