from django import forms
from .models import Deck

class NewDeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('name', 'finished')