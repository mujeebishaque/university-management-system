from django.contrib import admin
from library.models import Book
# Register your models here.

class BookModel(admin.ModelAdmin):
    list_display = ['bookTitle', 'bookAuthor', 'bookPublisher', '_datePublished']
    list_filter = ['bookTitle', 'bookAuthor']
    search_fields = ['bookTitle', 'bookAuthor']

admin.site.register(Book, BookModel)