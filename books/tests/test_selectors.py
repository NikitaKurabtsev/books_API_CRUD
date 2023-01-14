from django.test import TestCase

from books.models import Author, Book
from books.selectors import AuthorSelector, BookSelector


class SelectorTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='test_author'
        )
        self.book = Book.objects.create(
            name='test_book',
            category='Drama',
            release_date='2001-01-01',
            author=self.author,
            is_read=True
        )

    def test_get_author(self):
        self.assertEqual(AuthorSelector.get_author(self.author.name), 
                         Author.objects.first())

    def test_get_book(self):
        self.assertEqual(BookSelector.get_book(id=1), self.book)

    def test_get_authors_books_count(self):
        authors = AuthorSelector.get_authors()
        self.assertEqual(authors[0].books_count, 1)
