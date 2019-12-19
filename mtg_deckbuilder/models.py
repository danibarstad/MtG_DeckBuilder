from django.db import models
from django.contrib.auth.models import User
from . import mtg_api
from multiselectfield import MultiSelectField

User._meta.get_field('username')._unique = True
User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False



class Deck(models.Model):
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)    # User
    name = models.CharField(max_length=100)                                         # Deck title
    text = models.CharField(max_length=100)                                         # Deck description
    cardList = MultiSelectField('Cards', choices=mtg_api.get_card_list())           # Cards to choose from

    def __str__(self):
        return f'{self.name}'