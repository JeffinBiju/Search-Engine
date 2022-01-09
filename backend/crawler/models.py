from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.TextField(unique = True)

    def _str_(self):
        return self.url

class Site(models.Model):
    site = models.TextField()

    def _str_(self):
        return self.site

