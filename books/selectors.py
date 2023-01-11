from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from books.models import Author, Book


class BookSelector:
    @staticmethod
    def get_books() -> QuerySet[Book]:
        """
        Return all objects of Book model.
        """
        books = Book.objects.select_related('author').all()
        
        return books

    @staticmethod
    def get_book(id: int) -> Book:
        """
        Return detail object of Book model.
        """
        book = get_object_or_404(Book, pk=id)

        return book


class AuthorSelector:
    @staticmethod
    def get_authors() -> QuerySet[Author]:
        """
        Return all authors with annotate books count field.
        """
        authors = Author.objects.annotate(books_count=Count('books'))
        
        return authors

    @staticmethod
    def get_author(author: str) -> Author:
        """
        Return Author model object.
        """
        book_author = Author.objects.get(name__iexact=author)

        return book_author
