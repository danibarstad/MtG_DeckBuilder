from django.db import models
from django.contrib.auth.models import User
from . import mtg_api
from multiselectfield import MultiSelectField

User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

cards = []
cardList = mtg_api.get_card_list()
for card in cardList:
        cards.append(('name', card.name))

class Deck(models.Model):
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    cardList = MultiSelectField(choices=cards)

    def __str__(self):
        return f'{self.name}'