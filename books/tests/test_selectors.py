from django.test import TestCase

from books.models import Author, Book
from books.selectors import get_book, get_book_author, get_authors_books_count


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
        self.assertEqual(get_book_author(self.author.name), Author.objects.first())

    def test_get_book(self):
        self.assertEqual(get_book(id=3), self.book)

    def test_get_authors_books_count(self):
        author_books_count = get_authors_books_count()
        self.assertEqual(author_books_count[0].books_count, 1)
