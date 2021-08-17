from django.db import models
from django.shortcuts import redirect, render
from .models import Book, Author

# Books 
def index(request):
    context = {
        'all_books' : Book.objects.all(),
        # 'authors' : Author.objects.all()
    }
    return render(request, "books.html", context)

def create_book(request):
    if request.method == "POST":
        Book.objects.create (title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')


def view_book(request, book_id):
    context = {
        'book' : Book.objects.get(id = book_id),
        'authors' : Book.objects.get(id = book_id).authors.all(),
        'all_authors' : Author.objects.all(),
        'book_id' : book_id
    }
    return render(request, "book_display.html", context)

def add_author(request):
    newAuth = Author.objects.get(id = request.POST['author'])
    authsBook = Book.objects.get(id = request.POST['book'])
    authsBook.authors.add(newAuth)
    return redirect (f"view_book/{authsBook.id}")


# Authors
def authors(request):
    context = {
        'all_authors' : Author.objects.all(),
    }
    return render(request, "authors.html", context)

def create_author(request):
    if request.method == "POST":
        Author.objects.create (first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/authors')

def view_author(request, author_id):
    context = {
        'author' : Author.objects.get(id = author_id),
        'book' : Author.objects.get (id = author_id).books.all(),
        'all_books' : Book.objects.all(),
        'author_id' : author_id
    }
    return render(request, "author_display.html", context)

def add_book(request):
    newBook = Book.objects.get(id = request.POST['book'])
    booksAuth = Author.objects.get(id = request.POST['author'])
    booksAuth.books.add(newBook)
    return redirect (f"view_author/{booksAuth.id}")
