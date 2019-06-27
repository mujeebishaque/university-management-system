from django.db import models

# Create your models here.

class Book(models.Model):
    
    bookTitle = models.CharField(max_length=256)
    bookAuthor = models.CharField(max_length=128)
    bookPublisher = models.CharField(blank=True, max_length=64)
    _datePublished = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bookTitle