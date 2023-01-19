from django.core.exceptions import ValidationError
from django.test import TestCase

from books.models import Author, Book


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='test_author'
        )

    def test_author_model_to_string(self):
        self.assertEqual(str(self.author), 'test_author')

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='test_author')
        self.book = Book.objects.create(
            name='book',
            category='Drama',
            release_date='2005-01-01',
            author=self.author,
            is_read=True
        )
        self.book_for_validate = Book.objects.create(
            name='book',
            category='Drama',
            release_date='2025-01-01',
            author=self.author,
            is_read=True
        )

    def test_book_model_to_string(self):
        self.assertEqual(str(self.book), 'book')

    def test_book_release_date_cannot_be_later_than_today(self):
        self.assertRaises(ValidationError, self.book_for_validate.clean)

