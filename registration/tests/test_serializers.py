from django.urls import reverse
from test_plus.test import TestCase as PlusTestCase

from registration.serializers import RegisterSerializer


class RegisterSerializerTest(PlusTestCase):
    def setUp(self):
        self.url = reverse('registration:registration')
        self.user_data = {
                'username': 'test_user2',
                'password': 'testpassword2', 
                'password2': 'testpassword2', 
                'email': 'test2@gmail.com', 
                'first_name': 'test_first_name2', 
                'last_name': 'test_last_name2',
            }
    
    def test_correct_serializer_validation(self):
        serializer = RegisterSerializer(data=self.user_data)

        self.assertEqual(serializer.is_valid(), True)

    def test_incorrect_serializer_validation(self):
        self.user_data['password2'] = 'incorrect_password'
        serializer = RegisterSerializer(data=self.user_data)

        self.assertFalse(serializer.is_valid())
