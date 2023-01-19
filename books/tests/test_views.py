from unittest import mock
import datetime

from django.urls import reverse
from faker import Faker
from test_plus.test import TestCase as PlusTestCase

from books.models import Author, Book
from books.services import AuthorService, BookService

faker = Faker()


class AuthorListApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('authors:list')
  
    def test_author_list_view(self):
        self.client.get(self.url)
        self.response_200


class AuthorCreateApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('authors:create')
        self.data = {'name': faker.pystr(max_chars=20)}
        self.user = self.make_user('user')

    def test_author_create_view(self):
        self.client.post(self.url, data=self.data)
        self.response_201

    @mock.patch('books.views.AuthorService.create_author',
                wraps=AuthorService.create_author)
    def test_view_calls_create_author_service(self, service_mock):
        with self.login(self.user):
            self.client.post(self.url, data=self.data)
        service_mock.assert_called_once_with(**self.data)


class BookListApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books:list')

    def test_book_list_api(self):
        self.client.get(self.url)
        self.response_200


class BookCreateApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books:create')
        self.author = Author.objects.create(name=faker.pystr(max_chars=20))
        self.user = self.make_user('user')
        self.data = {
            'name': faker.pystr(max_chars=20),
            'category': 'Drama',
            'release_date': datetime.date(2001, 1, 1),
            'author': self.author.name,
            'is_read': True
        }

    def test_book_create_view(self):
        self.client.post(self.url, data=self.data)
        self.response_201

    @mock.patch('books.views.BookService.create_book', 
                wraps=BookService.create_book)
    def test_view_calls_create_book_service(self, service_mock):
        with self.login(self.user):
            self.client.post(self.url, data=self.data)
        service_mock.assert_called_once_with(**self.data)


class BookDetailApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books:update', args=['1'])

    def test_book_detail_view(self):
        self.client.get(self.url)
        self.response_200


class BookUpdateApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books:update', args=['1'])
        self.user = self.make_user('user')
        self.author = Author.objects.create(name=faker.pystr(max_chars=20))
        self.book = Book.objects.create(
            name=faker.pystr(max_chars=20),
            category='Drama',
            author=self.author,
            release_date=datetime.date(2001, 1, 1),
            is_read=True
        )
        self.updated_data = {
            'id': self.book.pk,
            'name': self.book.name,
            'category': self.book.category,
            'author': self.author.name,
            'release_date': self.book.release_date,
            'is_read': False
        }

    def test_book_update_view(self):
        self.client.post(self.url, data=self.updated_data)
        self.response_200

    @mock.patch('books.views.BookService.update_book',
                wraps=BookService.update_book)
    def test_view_calls_update_service(self, service_mock):
        with self.login(self.user):
            self.client.put(self.url, data=self.updated_data,
                            content_type='application/json')
        service_mock.assert_called_once_with(**self.updated_data)


class BookDeleteApiTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books:delete', args=['1'])
        self.user = self.make_user('user')
        self.author = Author.objects.create(name=faker.pystr(max_chars=20))
        self.book = Book.objects.create(
            name=faker.pystr(max_chars=20),
            category='Drama',
            author=self.author,
            release_date=datetime.date(2001, 1, 1),
            is_read=True
        )

    def test_book_delete_view(self):
        self.client.delete(self.url)
        self.response_204

    @mock.patch('books.views.BookService.delete_book', 
                wraps=BookService.delete_book)
    def test_view_calls_delete_service(self, service_mock):
        with self.login(self.user):
            self.client.delete(self.url)
        service_mock.assert_called()
