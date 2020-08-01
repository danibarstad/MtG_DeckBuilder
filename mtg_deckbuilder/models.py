from . import mtg_api
from django.db import models
from multiselectfield import MultiSelectField



class Deck(models.Model):
    user = models.CharField(max_length=100)                                         # User
    name = models.CharField(max_length=100)                                         # Deck title
    text = models.CharField(max_length=100)                                         # Deck description
    cardList = MultiSelectField('Cards', choices=mtg_api.get_card_list())           # Cards to choose from

    def __str__(self):
        return f'{self.name}'