from django.test import TestCase

from django.contrib.auth.models import User
from django.db import IntegrityError


class TestUser(TestCase):

    def test_create_user_duplicate_username(self):
        dani = User(username='dani', email='dani@dani.dani', first_name='dani', last_name='dani')
        dani.save()

        dani2 = User(username='dani', email='dani2@dani.dani', first_name='dani', last_name='dani')
        with self.assertRaises(IntegrityError):
            dani2.save()
    
    # def test_create_user_duplicate_username_case_insensitive(self):

    # def test_create_user_duplicate_email_case_insensitive(self):

    def test_create_user_duplicate_email(self):
        dani = User(username='dani', email='dani@dani.dani', first_name='dani', last_name='dani')
        dani.save()

        dani2 = User(username='dani2', email='dani@dani.dani', first_name='dani', last_name='dani')
        with self.assertRaises(IntegrityError):
            dani2.save()