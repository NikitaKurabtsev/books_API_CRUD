from unittest import mock

from django.urls import reverse
from faker import Faker
from test_plus.test import TestCase as PlusTestCase
from books.models import Author

from books.views import AuthorListApiView

faker = Faker()


class AuthorListApiViewTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('authors')
        self.data = {
            'name': faker.pystr(max_chars=20)
        }

    def test_api_view_can_be_accessed(self):
        self.client.get(self.url)
        self.response_200

    def test_api_view_can_create(self):
        self.client.post(self.url, data=self.data)
        self.response_201

    # @mock.patch('books.views.AuthorListApiView.create_author')
    # def test_view_calls_service(self, service_mock):
    #     self.post(self.url, data=self.data)
    #     service_mock.assert_called_once_with(**self.data)


class BooksListApiViewTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('books')
        self.author = Author.objects.create(name=faker.pystr(max_chars=20))
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

