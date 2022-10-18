from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from books.models import Author, Book


def get_books() -> QuerySet[Book]:
    """
    Return all objects of Book model.
    """
    books = Book.objects.select_related('author').all()
    
    return books


def get_book(id: int) -> Book:
    """
    Return detail object of Book model.
    """
    book = get_object_or_404(Book, pk=id)

    return book


def get_authors_books_count() -> QuerySet[Author]:
    """
    Return all authors with annotate books count field.
    """
    authors = Author.objects.annotate(books_count=Count('books'))
    
    return authors


def get_book_author(author) -> Author:
    """
    Return Author model object.
    """
    author = Author.objects.get(name__iexact=author)

    return author
