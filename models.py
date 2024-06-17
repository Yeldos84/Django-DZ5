from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField("date published")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField("date published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField("date published")
    status = models.CharField(max_length=100)
    borrower = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.imprint

class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name


