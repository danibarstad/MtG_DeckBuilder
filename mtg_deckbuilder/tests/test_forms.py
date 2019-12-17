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