import imp
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from faker import Faker


fake = Faker()


class UserRegisterAPIViewTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user',
            password='testpassword',  
            email='test@gmail.com', 
            first_name='test_first_name', 
            last_name='test_last_name',
        )
        self.url = reverse('auth_register')
        self.client.login(username='test_user', password='testpassword')

    def test_create_user(self):
        data = {
            'username': 'test_user2',
            'password': 'testpassword2', 
            'password2': 'testpassword2', 
            'email': 'test2@gmail.com', 
            'first_name': 'test_first_name2', 
            'last_name': 'test_last_name2',
        }
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username', ''), data.get('username', ''))
        self.assertEqual(response.data.get('email', ''), data.get('email', ''))
        self.assertFalse('password' in response.data)
