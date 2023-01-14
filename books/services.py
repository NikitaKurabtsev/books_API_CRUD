from datetime import date

from django.shortcuts import get_object_or_404

from books.models import Author, Book
from books.selectors import AuthorSelector, BookSelector


class AuthorService:
    @staticmethod
    def create_author(name: str) -> Author:
        """
        Create a Author model object.
        """
        author = Author(name=name)
        author.full_clean()
        author.save()

        return author

    @staticmethod
    def delete_author(id: int) -> None:
        author = get_object_or_404(Author, id=id)
        author.delete()


class BookService:
    @staticmethod
    def create_book(name: str, release_date: date, is_read: bool, 
                    category: str, author: str) -> Book:
        """
        Create a Book model object with own logic.
        """
        book_author = AuthorSelector.get_author(author=author)

        book = Book(
            name=name, 
            release_date=release_date, 
            is_read=is_read, 
            category=category, 
            author=book_author
        )

        book.full_clean()
        book.save()

        return book

    @staticmethod
    def update_book(id: int, name: str, release_date: date, is_read: bool, 
                    category: str, author: str) -> Book:
        """
        Update a Book model object with own logic.
        """
        book = BookSelector.get_book(id=id)
        book_author = AuthorSelector.get_author(author=author)

        book.name = name
        book.release_date = release_date
        book.is_read = is_read
        book.category = category
        book.author = book_author

        book.full_clean()
        book.save()

        return book

    @staticmethod
    def delete_book(id: int) -> None:
        """
        Delete a Book model object.
        """
        book = get_object_or_404(Book, pk=id)
        book.delete()
