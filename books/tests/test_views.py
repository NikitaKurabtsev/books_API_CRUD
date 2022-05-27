
from unittest import mock

from django.urls import reverse
from faker import Faker
from test_plus.test import TestCase as PlusTestCase
from books.models import Author, Book
from books.services import create_author

from books.views import AuthorListApiView

faker = Faker()


class AuthorListApiViewTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('authors')
        self.data = {
            'name': faker.pystr(max_chars=20)
        }
        self.user = self.make_user('user')

    def test_api_view_can_be_accessed(self):
        self.client.get(self.url)
        self.response_200

    def test_api_view_can_create(self):
        self.client.post(self.url, data=self.data)
        self.response_201

    @mock.patch('books.views.create_author', wraps=create_author)
    def test_view_calls_service(self, service_mock):
        with self.login(self.user):
            response = self.client.post(self.url, data=self.data)
            print(response.status_code)
        # self.assertTrue(Author.objects.filter(**self.data).exists())
        service_mock.assert_called_once_with(name=self.data['name'])
        


class BooksListApiViewTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books')
        self.author = Author.objects.create(
            name=faker.pystr(max_chars=20)
        )
        self.data = {
            'name': faker.pystr(max_chars=20),
            'category': 'Drama',
            'author': self.author,
            'release_date': faker.date,
            'is_read': True
        }

    def test_api_view_can_be_accessed(self):
        self.client.get(self.url)
        self.response_200

    def test_api_view_can_create(self):
        self.client.post(self.url, data=self.data)
        self.response_201


class BooksDetailApiViewTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books-detail', args=['1'])
        self.author = Author.objects.create(
            name=faker.pystr(max_chars=20)
        )
        self.book = Book.objects.create(
            name=faker.pystr(max_chars=20),
            category='Drama',
            author=self.author,
            release_date='2000-01-02',
            is_read=True
        )
        self.updated_data = {
            'name': faker.pystr(max_chars=20),
            'category': 'Drama',
            'author': self.author,
            'release_date': '2000-01-03',
            'is_read': True
        }

    def test_api_view_can_be_accessed(self):
        self.client.get(self.url)
        self.response_200

    def test_api_view_can_update(self):
        self.client.post(self.url, data=self.updated_data)
        self.response_200

    def test_api_view_can_delete(self):
        self.client.delete(self.url)
        self.response_204
