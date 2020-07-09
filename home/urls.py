from django.urls import path
from . import views
 #check out naming routes in django routes
 #u might use a form to bring back the id of the book/author u want
 #within its value by using {{Books get ID}}
 #and display it using the post which can bring up the book/author
urlpatterns = [
    path('', views.index),
    path('books/<int:bookId>/', views.books),
    path('books/<int:bookId>/addAuthor', views.addAuthor2book),
    path('authors/<int:authorId>/', views.authorInfo), 
    path('authors/<int:authorId>/addBook', views.addBook2Author)  ,
    path('authors', views.authors),
    path('newBook', views.newBook)
]