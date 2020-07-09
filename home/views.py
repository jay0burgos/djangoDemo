from django.shortcuts import render, redirect
from .models import Author, Book

def index(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def authorInfo(request, authorId):
    thisAuthor = Author.objects.get(id = authorId)
    context={
        'books' : Book.objects.all(),
        'author': thisAuthor,
        'author_books':thisAuthor.books.all()
    }
    return render(request, 'authorInfo.html', context)

def books(request, bookId):
    #use id to figure out the book

    thisBook = Book.objects.get(id = bookId) 
    
    context={
        'authors': Author.objects.all(),
        'book': thisBook,
        'book_authors': thisBook.authors.all()
    }
    return render(request, 'books.html', context)

def addAuthor2book(request, bookId):
    authorID = request.POST['authors']
    bookID = request.POST['book_id']
    author = Author.objects.get(id = authorID)
    book = Book.objects.get(id = bookID)
    book.authors.add(author)
    book.save()
    return redirect('/books/'+bookID+'/')

def addBook2Author(request, authorId):
    bookID = request.POST['book']
    book = Book.objects.get(id=bookID)
    author = Author.objects.get(id = authorId)
    author.books.add(book)
    author.save()
    return redirect('/authors/' + str(authorId) + '/')

def authors(request):
    context={
        'authors': Author.objects.all(),
    }
    return render(request, 'authors.html', context)


def newBook(request):
    Book.objects.create(title = request.POST['title'], desc= request.POST['desc'])
    return redirect('/')
def newAuthor(request):
    Author.objects.create(name = request.POST['name'])

