from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from books.models import Author, Book


class BookSelector:
    @staticmethod
    def get_books() -> QuerySet[Book]:
        """
        Returns all books.
        """
        books = Book.objects.select_related('author').all()
        
        return books

    @staticmethod
    def get_book(id: int) -> Book:
        """
        Returns the book.
        """
        book = get_object_or_404(Book, pk=id)

        return book


class AuthorSelector:
    @staticmethod
    def get_authors() -> QuerySet[Author]:
        """
        Returns all authors with count of their books.
        """
        authors = Author.objects.annotate(books_count=Count('books'))
        
        return authors

    @staticmethod
    def get_author(author: str) -> Author:
        """
        Returns the author.
        """
        book_author = Author.objects.get(name__iexact=author)

        return book_author
