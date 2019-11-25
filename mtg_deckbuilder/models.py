from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False


class Deck(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, finished? {self.finished}'