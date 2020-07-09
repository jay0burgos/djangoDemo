from django.db import models

# Create your models here.
#books-title text
#authors-name
class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)

class Author(models.Model):
    name=models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)