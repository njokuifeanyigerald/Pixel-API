from urllib import response
from app.models import ImageModel
from .test_setup import TestSetup
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User


class TestView(TestSetup):

    def test_unauthenticated_user_cannot_post(self):
        res  = self.client.post(self.anyone_url)
        self.assertEqual(res.status_code, 405)
    def test_unauthenticated_user_can_get_data(self):
        res  = self.client.get(self.anyone_url)
        self.assertEqual(res.status_code, 200)

