from django.test import TestCase
from django.shortcuts import get_object_or_404

from books.models import Author, Book
from books.selectors import AuthorSelector, BookSelector
from books.services import AuthorService, BookService


class BookServiceTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='test_author'
        )
        self.book_to_create = {
            'name': 'test_book',
            'category': 'Drama',
            'release_date': '2001-01-01',
            'author': self.author,
            'is_read': True
        }
        self.book_to_update = {
            'name': 'updated_book',
            'category': 'Drama',
            'release_date': '2001-01-01',
            'author': self.author,
            'is_read': True
        }
        self.book = Book.objects.create(
            name='book',
            category='Drama',
            release_date='2005-01-01',
            author=self.author,
            is_read=True
        )

    def test_create_book_service(self):
        new_book = BookService.create_book(**self.book_to_create)

        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(new_book.name, self.book_to_create['name'])

    def test_update_book_service(self):
        book = Book.objects.filter(name='book').first()
        updated_book = BookService.update_book(book.id, **self.book_to_update)

        self.assertNotEqual(book.name, updated_book.name)

    def test_delete_book_service(self):
        book_for_delete = BookService.delete_book(id=self.book.id)

        self.assertFalse(book_for_delete)


class AuthorServiceTest(TestCase):
    def setUp(self):
        self.author_for_create = {'name': 'test_author'}
        self.author_for_delete = Author.objects.create(name='author')

    def test_create_author_service(self):
        created_author = AuthorService.create_author(**self.author_for_create)

        self.assertEquals(self.author_for_create.get('name'), created_author.name)

    def test_delete_author_service(self):
        author = AuthorService.delete_author(id=self.author_for_delete.id)

        self.assertFalse(author)
