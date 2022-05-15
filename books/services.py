from datetime import date
from django.shortcuts import get_object_or_404

from books.models import Book, Author
from books.selectors import get_book, get_book_author


def create_author(name: str) -> Author:
    """
    Create a Author model object.
    """
    author = Author(name=name)

    author.full_clean()
    author.save()

    return author


def create_book(
    name: str, 
    release_date: date, 
    is_read: bool, 
    category: str, 
    author: str
) -> Book:
    """
    Create a Book model with own logic.
    """
    book_author = get_book_author(author=author)

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


def update_book(
    id: int, 
    name: str, 
    release_date: date, 
    is_read: bool, 
    category: str, 
    author: str
) -> Book:
    """
    Update a Book model with own logic.
    """
    book = get_book(id=id)
    book_author = get_book_author(author=author)

    book.name = name
    book.release_date = release_date
    book.is_read = is_read
    book.category = category
    book.author = book_author

    book.full_clean()
    book.save()

    return book


def delete_book(id: int) -> None:
    """
    Delete a Book model object.
    """
    book = get_object_or_404(Book, pk=id)
    book.delete()
