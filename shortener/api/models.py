from django.db import models

class URLInfo(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.CharField(max_length=4096)