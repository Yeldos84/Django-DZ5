from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book, Publisher, User, BookInstance, Genre
from django import forms
from .forms import AuthorForm, BookForm, PublisherForm

# Create your views here.

models_name_dict = {
    'Author': "Author",
    'Book': "Book",
    'Publisher': "Publisher"
}



def main(request):
    return render(request, "library/main.html")


def index(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            save_db(form)
            name = form.cleaned_data['name']
            # return redirect('/users/succes', {'form': form})
            return render(request, "library/succes.html", {"form": form, "name": name})
    else:
        form = AuthorForm()
        html_name = models_name_dict.get('Author')
        return render(request, "library/check.html", {"form": form, "html_name": html_name})

def succes(request):
    return render(request, 'library/succes.html')



def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            save_books(form)
            title = form.cleaned_data['title']
            # return redirect('/users/succes', {'form': form})
            return render(request, "library/succes.html", {"form": form, "title": title})
    else:
        form = BookForm()
        html_name = models_name_dict.get('Book')
        return render(request, "library/check.html", {"form": form, "html_name": html_name})


def publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            save_publisher(form)
            # title = form.cleaned_data['title']
            # return redirect('/users/succes', {'form': form})
            return render(request, "library/succes.html", {"form": form})
    else:
        form = PublisherForm()
        html_name = models_name_dict.get('Publisher')
        return render(request, "library/check.html", {"form": form, "html_name": html_name})

def save_db(form):
    name = form.cleaned_data['name']
    birth_date = form.cleaned_data['birth_date']
    Author.objects.create(name=name, birth_date=birth_date)

def save_books(form):
    title = form.cleaned_data['title']
    publication_date = form.cleaned_data['publication_date']
    author = form.cleaned_data['author']
    Book.objects.create(title=title, publication_date=publication_date,author=author)

def save_publisher(form):
    name = form.cleaned_data['name']
    address = form.cleaned_data['address']
    books = form.cleaned_data['books']
    Publisher.objects.create(name=name, address=address,books=books)


