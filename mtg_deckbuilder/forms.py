from . import mtg_api
from django import forms
from .models import Deck
from multiselectfield import MultiSelectField


#Form for user to create a new deck
class NewDeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('user', 'name', 'text', 'cardList')