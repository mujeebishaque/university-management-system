from django.db import models

# Create your models here.

class Headline(models.Model):

    headline = models.CharField(max_length=128)
    dateposted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline