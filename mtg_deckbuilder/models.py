from django.db import models

# Create your models here.

class Deck(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, finished? {self.finished}'