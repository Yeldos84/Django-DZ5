from django.contrib import admin
from .models import Author, Book, Publisher, User, BookInstance, Genre
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(User)
admin.site.register(BookInstance)
admin.site.register(Genre)