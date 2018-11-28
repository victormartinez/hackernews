from django.conf import settings
from django.db import models


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)
