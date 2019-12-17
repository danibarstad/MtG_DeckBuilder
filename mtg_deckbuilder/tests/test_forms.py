from django.test import TestCase

from django.contrib.auth.models import User
from mtg_deckbuilder.forms import NewDeckForm, UserRegistrationForm
import string


class NewDeckFormTests(TestCase):

    def test_missing_name_is_invalid(self):
        data = {"text": "this is text test"}
        form = NewDeckForm(data)
        self.assertFalse(form.is_valid())

        no_names = list(string.whitespace) + ['   ', '\n\n\n', '\t\n\t\n']

        for no_name in no_names:
            data = {"name" : no_name, "text": "text test"}
            form = NewDeckForm(data)
            self.assertFalse(form.is_valid())
    
    def test_missing_text_is_invalid(self):
        data = {"name": "name test"}
        form = NewDeckForm(data)
        self.assertFalse(form.is_valid())

        no_text = list(string.whitespace) + ['   ', '\n\n\n', '\t\n\t\n']

        for no_txt in no_text:
            data = {"name": "name test", "text": no_txt}
            form = NewDeckForm(data)
            self.assertFalse(form.is_valid())
    
    def test_name_too_long_invalid(self):
        data= {"name": "x" * 101}
        form = NewDeckForm(data)
        self.assertFalse(form.is_valid())
    
    def test_text_too_long_is_invalid(self):
        data = {"text": "x" * 101}
        form = NewDeckForm(data)
        self.assertFalse(form.is_valid())

    def test_name_text_is_valid(self):
        data = {"name": "test name", "text": "test text"}
        form = NewDeckForm(data)
        self.assertTrue(form.is_valid())


class RegistrationFormTests(TestCase):

    def test_register_with_valid_data(self):
        data = {'username': 'dani', 'email': 'dani@dani.dani', 'first_name': 'dani', 'last_name': 'dani', 'password1': 'danidanidani1', 'password2': 'danidanidani1'}
        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())
    
    def test_register_with_missing_data(self):
        data = {'username': 'dani', 'email': 'dani@dani.dani', 'first_name': 'dani', 'last_name': 'dani', 'password1': 'danidanidani1', 'password2': 'danidanidani1'}
        for field in data.keys():
            d = dict(data)
            del(d[field])
            form = UserRegistrationForm(d)
            self.assertFalse(form.is_valid())
    
    def test_register_with_wrong_password(self):
        data = {'username': 'dani', 'email': 'dani@dani.dani', 'first_name': 'dani', 'last_name': 'dani', 'password1': 'danidanidani1', 'password2': 'danidanidani2'}
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())

    def test_register_with_email_already_in_db(self):
        dani = User(username='dani', email='dani@dani.dani', first_name='dani', last_name='dani')
        dani.save()

        data = {'username': 'dani2', 'email': 'dani@dani.dani', 'first_name': 'dani', 'last_name': 'dani', 'password1': 'danidanidani1', 'password2': 'danidanidani1'}
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())
    
    def test_register_username_already_in_db(self):
        dani = User(username='dani', email='dani@dani.dani')
        dani.save()

        data = {'username': 'dani', 'email': 'dani2@dani.dani', 'first_name': 'dani', 'last_name': 'dani', 'password1': 'danidanidani1', 'password2': 'danidanidani1'}
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())