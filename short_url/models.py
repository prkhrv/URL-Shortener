from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class short_urls(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    short_url = models.CharField(max_length = 20)
    long_url = models.URLField("URL",unique = True)

    def __str__(self):
        return self.long_url
