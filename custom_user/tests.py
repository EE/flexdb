"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from custom_user.models import CustomUser
import json


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class MyTests(TestCase):
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(username='user1', email='user1@user.pl', password='user1')
        CustomUser.objects.create_user(username='user2', email='user2@user.pl', password='user2')

    def test_anonymus_visibility(self):
        c = self.client
        response = c.get('/accounts/users', follow=True)
        self.assertEqual(response.__class__.__name__, "Response")
        self.assertIsNone(response.context)
        #self.assertEqual(response.context['detail'], "Not found")

    def test_user2_access_to_itself(self):
        c = self.client
        c.login(username='user2', password='user2')
        link = "/accounts/users/{}".format(CustomUser.objects.get(username='user2').id)
        response = c.get(link, follow=True)
        dict = json.loads(response.content)
        self.assertEqual(dict['username'], "user2")
        c.logout()

    def test_user2_access_to_others(self):
        c = self.client
        c.login(username='user2', password='user2')
        link = "/accounts/users/{}".format(CustomUser.objects.get(username='user1').id)
        response = c.get(link, follow=True)
        dict = json.loads(response.content)
        self.assertEqual(dict['detail'], "Not found")
        c.logout()

    def test_delete_logged(self):
        c = self.client
        c.login(username='user2', password='user2')
        link = "/accounts/users/{}".format(CustomUser.objects.get(username='user2').id)
        c.delete(link, follow=True)
        response = c.get(link, follow=True)
        dict = json.loads(response.content)
        self.assertEqual(dict['username'], "user2")
        c.logout()

    def test_delete_anonymous(self):
        c = self.client
        link = "/accounts/users/{}".format(CustomUser.objects.get(username='user2').id)
        c.delete(link, follow=True)
        c.login(username='user2', password='user2')
        response = c.get(link, follow=True)
        dict = json.loads(response.content)
        self.assertEqual(dict['username'], "user2")
        c.logout()