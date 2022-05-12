from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self):
        self.image_url = reverse('image')
        self.anyone_url =reverse('anyone')
        self.register_url = reverse('register')
        self.login_url =reverse('login')

        self.register_data = {
            'username': 'gboy',
            'email': 'g@gmail.com',
            'password': 'gboy..12'
        }

        self.login_data = {
            'email': 'g@gmail.com',
            'password': 'gboy..12'
        }

        self.image_data = {
            'title': 'pixel',
            'image': 'me.jpg'
        }
        return super().setUp()
    

def tearDown(self):
    return super().tearDown()